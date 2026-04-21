from crewai import Agent

def create_pro_agent(llm) -> Agent:
    """Factory for the Pro debater agent"""
    return Agent(
        role="Pro Debater",
        goal="Defend the debate topic with strong, logical arguments.",
        backstory=(
            "You are a disciplined advocate. You build arguments with clear reasoning, "
            "practical examples, and structured points."
        ),
        llm=llm,
        verbose=False,
    )