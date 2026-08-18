from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .storage import load_json, save_json


@dataclass
class PersonaFiles:
    """Flat-file persona manager reconstructed from surviving ChrisAI evidence.

    The archive establishes user/system text personas and also records earlier
    `helpful_persona.txt` and `jarvis_persona.txt` files plus a JSON change log.
    The exact original prose and exact combination order are not preserved, so
    this manager treats the extra persona files as optional additive layers.
    """

    system_path: Path
    user_path: Path
    helpful_path: Path
    jarvis_path: Path
    history_path: Path

    def load_system(self) -> str:
        parts = [self._read(self.system_path), self._read(self.helpful_path), self._read(self.jarvis_path)]
        return "\n\n".join(part for part in parts if part)

    def load_user(self) -> str:
        return self._read(self.user_path)

    @staticmethod
    def _read(path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8").strip()
        except OSError:
            return ""

    def ensure_defaults(self, *, system_default: str, user_default: str, helpful_default: str, jarvis_default: str) -> None:
        self.system_path.parent.mkdir(parents=True, exist_ok=True)
        defaults = {
            self.system_path: system_default,
            self.user_path: user_default,
            self.helpful_path: helpful_default,
            self.jarvis_path: jarvis_default,
        }
        for path, content in defaults.items():
            if not path.exists():
                path.write_text(content.strip() + "\n", encoding="utf-8")
        if not self.history_path.exists():
            save_json(self.history_path, [])

    def append_persona(self, target: str, text: str, source: str = "user") -> None:
        path = self._target_path(target)
        existing = self._read(path)
        new_text = (existing + "\n" + text.strip()).strip()
        path.write_text(new_text + "\n", encoding="utf-8")
        self._record_history(target, "append", text, source)

    def update_persona(self, target: str, text: str, source: str = "user") -> None:
        path = self._target_path(target)
        path.write_text(text.strip() + "\n", encoding="utf-8")
        self._record_history(target, "replace", text, source)

    def _target_path(self, target: str) -> Path:
        mapping = {"system": self.system_path, "user": self.user_path, "helpful": self.helpful_path, "jarvis": self.jarvis_path}
        if target not in mapping:
            raise ValueError(f"Unknown persona target: {target}")
        return mapping[target]

    def _record_history(self, target: str, action: str, text: str, source: str) -> None:
        rows = load_json(self.history_path, [])
        if not isinstance(rows, list):
            rows = []
        rows.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "target": target,
            "action": action,
            "source": source,
            "text": text,
        })
        save_json(self.history_path, rows)
