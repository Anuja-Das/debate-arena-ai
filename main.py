from __future__ import annotations
from src.core.app import run_debate

def main() -> None:
    topic = input("Enter a debate topic: ").strip()
    if not topic:
        print("Please provide a valid topic.")
        return

    try:
        debate = run_debate(topic=topic)
    except Exception as e:
        print(f"Failed to run debate: {e}")
        print("Tip: ensure Ollama is running and the model is pulled locally.")
        return

    print()


if __name__ == "__main__":
    main()