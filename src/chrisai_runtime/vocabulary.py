from __future__ import annotations

import re


class VocabularyManager:
    """Small executable subset of the surviving August 2025 vocabulary logic."""

    def __init__(self) -> None:
        self.word_map = {
            "utilize": "use",
            "implement": "make",
            "facilitate": "help",
            "demonstrate": "show",
            "methodology": "method",
            "functionality": "feature",
            "initialize": "start",
            "terminate": "end",
            "configuration": "setup",
            "modification": "change",
            "authentication": "login process",
            "instantiate": "create",
            "concatenate": "join",
            "deprecated": "outdated",
            "approximately": "about",
            "execute": "run",
            "generate": "make",
            "validate": "check",
            "invoke": "call",
        }
        self.preserve_terms = {
            "python",
            "sql",
            "javascript",
            "html",
            "css",
            "api",
            "rest",
            "json",
            "xml",
            "yaml",
            "websocket",
            "git",
            "github",
            "docker",
            "ai",
            "ml",
            "model",
            "inference",
            "nexus",
            "synapse",
        }

    def simplify(self, text: str) -> str:
        result = text
        for complex_word, simple_word in self.word_map.items():
            if complex_word in self.preserve_terms:
                continue
            result = re.sub(
                rf"\b{re.escape(complex_word)}\b",
                simple_word,
                result,
                flags=re.IGNORECASE,
            )
        return result
