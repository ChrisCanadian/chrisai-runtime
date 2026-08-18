from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ChrisAIConfig:
    """Flat-file runtime configuration.

    The directory names mirror the surviving August 26, 2025 settings while
    avoiding machine-specific absolute paths from the historical workstation.
    """

    base_dir: Path
    max_memory_messages: int = 20
    model_backend: str = "echo"
    model_name: str = "qwen2.5:3b"
    ollama_url: str = "http://localhost:11434"

    @property
    def personas_dir(self) -> Path:
        return self.base_dir / "personas"

    @property
    def memory_dir(self) -> Path:
        return self.base_dir / "memory"

    @property
    def data_dir(self) -> Path:
        return self.base_dir / "data"

    @property
    def system_persona_path(self) -> Path:
        return self.personas_dir / "system_persona.txt"

    @property
    def user_persona_path(self) -> Path:
        return self.personas_dir / "user_persona.txt"

    @property
    def helpful_persona_path(self) -> Path:
        return self.personas_dir / "helpful_persona.txt"

    @property
    def jarvis_persona_path(self) -> Path:
        return self.personas_dir / "jarvis_persona.txt"

    @property
    def persona_history_path(self) -> Path:
        return self.personas_dir / "persona_history.json"

    @property
    def memory_path(self) -> Path:
        return self.memory_dir / "memory.json"

    @property
    def learning_path(self) -> Path:
        return self.data_dir / "learning_data.json"

    def ensure_layout(self) -> None:
        for path in (self.personas_dir, self.memory_dir, self.data_dir):
            path.mkdir(parents=True, exist_ok=True)

    @classmethod
    def from_env(cls, base_dir: str | Path = ".chrisai") -> "ChrisAIConfig":
        return cls(
            base_dir=Path(base_dir),
            max_memory_messages=int(os.getenv("CHRISAI_MAX_MEMORY", "20")),
            model_backend=os.getenv("CHRISAI_MODEL_BACKEND", "echo").strip().lower(),
            model_name=os.getenv("CHRISAI_MODEL", "qwen2.5:3b"),
            ollama_url=os.getenv("CHRISAI_OLLAMA_URL", "http://localhost:11434").rstrip("/"),
        )
