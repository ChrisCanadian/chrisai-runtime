import json
import urllib.request

import pytest

from chrisai_runtime.model import OllamaModelClient


class FakeResponse:
    def __init__(self, payload: dict):
        self._payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self) -> bytes:
        return json.dumps(self._payload).encode("utf-8")


def test_ollama_adapter_posts_expected_payload(monkeypatch):
    captured = {}

    def fake_urlopen(request, timeout):
        captured["url"] = request.full_url
        captured["method"] = request.get_method()
        captured["content_type"] = request.headers.get("Content-type")
        captured["timeout"] = timeout
        captured["payload"] = json.loads(request.data.decode("utf-8"))
        return FakeResponse({"response": "  hello from ollama  "})

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)

    client = OllamaModelClient("http://localhost:11434", "qwen2.5:3b", timeout_seconds=17)
    result = client.generate("PROMPT")

    assert result == "hello from ollama"
    assert captured == {
        "url": "http://localhost:11434/api/generate",
        "method": "POST",
        "content_type": "application/json",
        "timeout": 17,
        "payload": {"model": "qwen2.5:3b", "prompt": "PROMPT", "stream": False},
    }


def test_ollama_adapter_rejects_missing_text_response(monkeypatch):
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        lambda request, timeout: FakeResponse({"done": True}),
    )

    client = OllamaModelClient("http://localhost:11434", "qwen2.5:3b")

    with pytest.raises(RuntimeError, match="did not contain a text 'response' field"):
        client.generate("PROMPT")
