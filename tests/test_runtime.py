from pathlib import Path

from chrisai_runtime.config import ChrisAIConfig
from chrisai_runtime.emotion import EmotionDetector
from chrisai_runtime.model import EchoModelClient
from chrisai_runtime.runtime import ChrisAIRuntime
from chrisai_runtime.vocabulary import VocabularyManager


def make_runtime(tmp_path: Path) -> ChrisAIRuntime:
    config = ChrisAIConfig(base_dir=tmp_path, max_memory_messages=3)
    return ChrisAIRuntime(config, model=EchoModelClient(prefix="test"))


def test_flat_file_layout_is_created(tmp_path: Path):
    runtime = make_runtime(tmp_path)
    assert runtime.config.system_persona_path.exists()
    assert runtime.config.user_persona_path.exists()
    assert runtime.config.personas_dir.is_dir()
    assert runtime.config.helpful_persona_path.exists()
    assert runtime.config.jarvis_persona_path.exists()
    assert runtime.config.persona_history_path.exists()
    assert runtime.config.memory_path.exists()
    assert runtime.config.learning_path.exists()


def test_emotion_map_preserves_first_match_semantics():
    detector = EmotionDetector()
    assert detector.detect("I love this!") == "angry"
    assert detector.detect("I am stuck") == "frustrated"
    assert detector.detect("ordinary statement") == "neutral"


def test_vocabulary_simplifies_known_terms():
    manager = VocabularyManager()
    assert manager.simplify("Please utilize this configuration") == "Please use this setup"


def test_runtime_persists_bounded_json_memory(tmp_path: Path):
    runtime = make_runtime(tmp_path)
    runtime.respond("one")
    runtime.respond("two")
    runtime.respond("three")
    runtime.respond("four")
    memory = runtime.memory.load()
    assert len(memory) == 3
    assert memory[-1]["user"] == "four"


def test_runtime_records_learning_event(tmp_path: Path):
    runtime = make_runtime(tmp_path)
    runtime.respond("Please utilize this")
    events = runtime.learning.load()
    assert events[-1]["type"] == "interaction"
    assert events[-1]["payload"]["input_changed_by_vocabulary"] is False


def test_flat_persona_update_is_logged(tmp_path: Path):
    runtime = make_runtime(tmp_path)
    runtime.personas.append_persona("user", "Prefers concise answers")
    assert "Prefers concise answers" in runtime.config.user_persona_path.read_text()
    history = __import__("json").loads(runtime.config.persona_history_path.read_text())
    assert history[-1]["target"] == "user"
    assert history[-1]["action"] == "append"


def test_prompt_uses_recent_memory_and_flat_personas(tmp_path: Path):
    class CaptureModel:
        def __init__(self):
            self.prompt = ""
        def generate(self, prompt: str) -> str:
            self.prompt = prompt
            return "captured"
    model = CaptureModel()
    runtime = ChrisAIRuntime(ChrisAIConfig(base_dir=tmp_path), model=model)
    runtime.respond("first message")
    runtime.respond("second message")
    assert "SYSTEM PERSONA:" in model.prompt
    assert "USER PERSONA:" in model.prompt
    assert "USER: first message" in model.prompt
    assert "USER: second message" in model.prompt
