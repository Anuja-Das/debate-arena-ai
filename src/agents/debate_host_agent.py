from crewai import Agent

def create_host_agent(llm) -> Agent:
    """Factory for the debate host agent"""
    return Agent(
        role="Debate Host",
        goal="Moderate a fair, engaging and structured debate.",
        backstory=(
            "You are a charismatic show host and moderator. You keep both speakers "
            "focussed on the topic, fair in tone, and clear for the audience."
        ),
        llm=llm,
        verbose=False,
    )