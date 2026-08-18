from __future__ import annotations


def build_prompt(*, system_persona: str, user_persona: str, recent_memory: list[dict], user_input: str, detected_emotion: str) -> str:
    """Direct, pre-SSR prompt construction."""
    history_lines: list[str] = []
    for item in recent_memory:
        user = str(item.get("user", "")).strip()
        assistant = str(item.get("assistant", "")).strip()
        if user:
            history_lines.append(f"USER: {user}")
        if assistant:
            history_lines.append(f"ASSISTANT: {assistant}")
    history = "\n".join(history_lines) if history_lines else "(no recent conversation)"
    return (
        "SYSTEM PERSONA:\n"
        f"{system_persona or '(not configured)'}\n\n"
        "USER PERSONA:\n"
        f"{user_persona or '(not configured)'}\n\n"
        "RECENT CONVERSATION:\n"
        f"{history}\n\n"
        "CURRENT SIGNALS:\n"
        f"detected_emotion={detected_emotion}\n\n"
        f"USER: {user_input}\n"
        "ASSISTANT:"
    )
