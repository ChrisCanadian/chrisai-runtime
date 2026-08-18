from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .storage import load_json, save_json


@dataclass
class LearningLog:
    path: Path
    max_history: int = 1000

    def load(self) -> list[dict]:
        data = load_json(self.path, [])
        return data if isinstance(data, list) else []

    def record(self, event_type: str, payload: dict) -> None:
        rows = self.load()
        rows.append(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "type": event_type,
                "payload": payload,
            }
        )
        save_json(self.path, rows[-self.max_history :])
