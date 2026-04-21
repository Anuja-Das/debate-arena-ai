# debate-arena-ai

A multi-agent AI debate arena using CrewAI orchestration with a local Ollama model.

## What this demo does

1. Reads a debate topic from console input.
2. Runs three agents:
   - Debate Host
   - Pro Debater
   - Con Debater
3. Executes rounds:
   - Pro opening
   - Con opening
   - Pro rebuttal (responds to Con opening)
   - Con rebuttal (responds to Pro opening)
   - Host conclusion
4. Prints a transcript to the console.

## Project layout

- `main.py` - console entrypoint
- `src/core/app.py` - debate flow and task execution
- `src/core/llm_adapter.py` - CrewAI LLM adapter for Ollama
- `src/agents/*.py` - agent factories (host/pro/con)
- `src/config/llm_config.py` - model/provider/base URL settings
- `requirements.txt` - Python dependencies

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ollama setup

Make sure Ollama is running and the configured model is available.

Current defaults in `src/config/llm_config.py`:
- `llm_provider = "ollama"`
- `llm_model = "llama3.1"`
- `base_url = "http://127.0.0.1:11434"`

Pull the default model:

```powershell
ollama pull llama3.1
```

If you want another model (for example `mistral`), update `llm_model` in `src/config/llm_config.py` and pull it:

```powershell
ollama pull mistral
```

## Run

```powershell
python main.py
```

## Notes

- The app calls Ollama over HTTP using the base URL in `src/config/llm_config.py`.
- If startup fails, verify Ollama is running and the model exists locally.

## CrewAI one-liners

- Agent: who does the work
- Task: what work is done
- Crew: the team setup
- Process: the execution order
- Context: shared memory between tasks
