# debate-arena-ai

A simple local multi-agent AI debate demo using:
- CrewAI (orchestration)
- Ollama local model (`llama3.1` or `mistral`)

## What this demo does

1. Reads a debate topic from `input()`.
2. Runs three agents:
    - Debate Host Agent
    - Pro Agent
    - Con Agent
3. Executes rounds:
    - Pro opening argument
    - Con opening argument
    - Pro rebuttal (references Con opening)
    - Con rebuttal (references Pro opening)
    - Host summary and balanced conclusion
4. Prints a formatted transcript to the console.

## Project layout

- `demo_debate/main.py` - console entrypoint
- `demo_debate/app.py` - LLM setup, agents, tasks, crew execution, formatting
- `requirements.txt` - Python dependencies

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Make sure Ollama is running and a local model is available.

```powershell
ollama pull llama3.1
# or
ollama pull mistral
```

Run the demo:

```powershell
python -m demo_debate.main
```


## Notes

- This demo keeps existing code untouched and lives in the new `demo_debate` package.
- If your environment already has dependencies installed, you can skip reinstalling.

## CrewAI one-liner definitions:
- Agent → “Who is doing the work?”
- Task → “What work is being done?”
- Crew → “The whole team setup”
- Process → “Execution order”
- Context → “Shared memory between tasks”