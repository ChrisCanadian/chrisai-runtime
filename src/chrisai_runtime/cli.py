from __future__ import annotations

from .runtime import ChrisAIRuntime


def main() -> None:
    runtime = ChrisAIRuntime.create()
    print("ChrisAI historical reconstruction. Type /quit to exit.")
    while True:
        try:
            text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if text.lower() in {"/quit", "/exit"}:
            break
        if not text:
            continue
        print(f"ChrisAI: {runtime.respond(text)}")


if __name__ == "__main__":
    main()
