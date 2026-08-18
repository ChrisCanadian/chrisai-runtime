from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Protocol


class ModelClient(Protocol):
    def generate(self, prompt: str) -> str: ...


@dataclass
class EchoModelClient:
    """Deterministic test adapter; not a historical model claim."""

    prefix: str = "ChrisAI(test)"

    def generate(self, prompt: str) -> str:
        user_lines = [line for line in prompt.splitlines() if line.startswith("USER: ")]
        current = user_lines[-1][6:] if user_lines else prompt[-120:]
        return f"{self.prefix}: {current}"


@dataclass
class OllamaModelClient:
    base_url: str
    model: str
    timeout_seconds: int = 120

    def generate(self, prompt: str) -> str:
        payload = json.dumps({"model": self.model, "prompt": prompt, "stream": False}).encode("utf-8")
        request = urllib.request.Request(
            f"{self.base_url}/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                body = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"Local model request failed: {exc}") from exc
        text = body.get("response")
        if not isinstance(text, str):
            raise RuntimeError("Local model response did not contain a text 'response' field")
        return text.strip()
