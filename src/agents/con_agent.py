from crewai import Agent

def create_con_agent(llm) -> Agent:
    """Factory for the Con debator agent"""
    return Agent(
        role="Con Debater",
        goal="Challenge the debate topic with critical, logical objections.",
        backstory=(
            "You are a careful critic. You identify weak assumptions, trade-offs, "
            "and possible risks in claims made by the opposing side."
        ),
        llm=llm,
        verbose=False,
    )