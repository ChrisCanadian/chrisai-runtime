from __future__ import annotations


class EmotionDetector:
    """Conservative reconstruction of the pre-migration rule map.

    The October 4, 2025 snapshot records these categories, trigger examples,
    case-insensitive substring matching, first-match-wins semantics, and a
    neutral fallback.
    """

    def __init__(self) -> None:
        self.emotion_map: list[tuple[str, tuple[str, ...]]] = [
            ("angry", ("hate", "annoyed", "furious", "!")),
            ("sad", ("upset", "depressed", "unhappy", "tired")),
            ("curious", ("wonder", "why", "how", "what")),
            ("happy", ("love", "excited", "great", "awesome")),
            ("frustrated", ("confused", "stuck", "don't get it")),
        ]

    def detect(self, text: str) -> str:
        lowered = text.lower()
        for emotion, triggers in self.emotion_map:
            if any(trigger in lowered for trigger in triggers):
                return emotion
        return "neutral"
