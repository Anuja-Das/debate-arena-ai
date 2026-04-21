from typing import Any
from crewai import LLM
from src.config.llm_config import base_url, llm_model, llm_provider, temperature

def _build_chat_ollama() -> Any:
    """Create a CrewAI LLM configured to talk to the local Ollama instance"""
    model_id = llm_model if "/" in llm_model else f"{llm_provider}/{llm_model}"
    return LLM(
        model=model_id,
        base_url=base_url,
        temperature=temperature
    )