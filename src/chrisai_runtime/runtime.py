from __future__ import annotations

from importlib import resources
from pathlib import Path

from .config import ChrisAIConfig
from .emotion import EmotionDetector
from .learning import LearningLog
from .memory import ConversationMemory
from .model import EchoModelClient, ModelClient, OllamaModelClient
from .persona import PersonaFiles
from .prompt import build_prompt
from .storage import save_json
from .vocabulary import VocabularyManager


class ChrisAIRuntime:
    """Executable reconstruction of the flat-file ChrisAI response path."""

    def __init__(self, config: ChrisAIConfig, model: ModelClient | None = None) -> None:
        self.config = config
        self.config.ensure_layout()
        self.personas = PersonaFiles(
            system_path=config.system_persona_path,
            user_path=config.user_persona_path,
            helpful_path=config.helpful_persona_path,
            jarvis_path=config.jarvis_persona_path,
            history_path=config.persona_history_path,
        )
        self._ensure_persona_templates()
        if not config.memory_path.exists():
            save_json(config.memory_path, [])
        if not config.learning_path.exists():
            save_json(config.learning_path, [])
        self.memory = ConversationMemory(config.memory_path, config.max_memory_messages)
        self.learning = LearningLog(config.learning_path)
        self.emotion = EmotionDetector()
        self.vocabulary = VocabularyManager()
        self.model = model or self._build_model()

    def _ensure_persona_templates(self) -> None:
        defaults = resources.files("chrisai_runtime.defaults")
        system_default = defaults.joinpath("system_persona.txt").read_text(encoding="utf-8")
        user_default = defaults.joinpath("user_persona.txt").read_text(encoding="utf-8")
        helpful_default = defaults.joinpath("helpful_persona.txt").read_text(encoding="utf-8")
        jarvis_default = defaults.joinpath("jarvis_persona.txt").read_text(encoding="utf-8")
        self.personas.ensure_defaults(
            system_default=system_default,
            user_default=user_default,
            helpful_default=helpful_default,
            jarvis_default=jarvis_default,
        )

    def _build_model(self) -> ModelClient:
        if self.config.model_backend == "ollama":
            return OllamaModelClient(self.config.ollama_url, self.config.model_name)
        return EchoModelClient()

    def respond(self, user_input: str) -> str:
        raw_input = user_input.strip()
        if not raw_input:
            return ""
        emotion = self.emotion.detect(raw_input)
        # VocabularyManager existed in the era, but its exact hot-path placement
        # is not preserved strongly enough to claim automatic input rewriting.
        normalized_input = raw_input
        prompt = build_prompt(
            system_persona=self.personas.load_system(),
            user_persona=self.personas.load_user(),
            recent_memory=self.memory.recent(limit=5),
            user_input=normalized_input,
            detected_emotion=emotion,
        )
        response = self.model.generate(prompt)
        self.memory.append_exchange(raw_input, response, emotion)
        self.learning.record(
            "interaction",
            {"emotion": emotion, "input_changed_by_vocabulary": normalized_input != raw_input},
        )
        return response

    @classmethod
    def create(cls, base_dir: str | Path = ".chrisai") -> "ChrisAIRuntime":
        return cls(ChrisAIConfig.from_env(base_dir))
