from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .storage import load_json, save_json


@dataclass
class ConversationMemory:
    path: Path
    max_messages: int = 20

    def load(self) -> list[dict]:
        data = load_json(self.path, [])
        return data if isinstance(data, list) else []

    def recent(self, limit: int = 5) -> list[dict]:
        return self.load()[-limit:]

    def append_exchange(self, user: str, assistant: str, emotion: str) -> None:
        messages = self.load()
        messages.append(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "user": user,
                "assistant": assistant,
                "emotion": emotion,
            }
        )
        save_json(self.path, messages[-self.max_messages :])
