from __future__ import annotations
from dataclasses import dataclass
import time
from crewai import Task
from src.agents.con_agent import create_con_agent
from src.agents.pro_agent import create_pro_agent
from src.agents.debate_host_agent import create_host_agent
from src.core.llm_adapter import _build_chat_ollama
from src.core.prompts import (
    con_rebuttal_prompt,
    con_opening_prompt,
    pro_rebuttal_prompt,
    pro_opening_prompt,
    host_final_prompt
)

@dataclass
class DebateOutput:
    host_intro: str
    pro_opening: str
    con_opening: str
    pro_rebuttal: str
    con_rebuttal: str
    host_conclusion: str


def run_debate(topic: str) -> DebateOutput:
    """run debate sequentially (no Crew kickoff)"""
    llm = _build_chat_ollama()

    pro_agent = create_pro_agent(llm)
    con_agent = create_con_agent(llm)
    host_agent = create_host_agent(llm)

    host_intro = (
        f"\nWelcome to Debate Arena AI!\n"
        f"Today's topic: \"{topic}\"\n"
        f"Let's begin!\n"
    )
    print(host_intro)
    time.sleep(1)

    # PRO Opening
    print("=" * 25)
    print("===== ROUND 1: OPENING\n")
    print("=" * 25)
    print("===== PRO is thinking...\n")
    pro_opening = pro_agent.execute_task(
        Task(
            description=pro_opening_prompt.format(topic=topic),
            expected_output="A strong opening argument",
            agent=pro_agent
        )
    )
    print("===== PRO:\n", pro_opening, "\n")
    time.sleep(1)

    # CON Opening
    print("===== CON is thinking...\n")
    con_opening = con_agent.execute_task(
        Task(
            description=con_opening_prompt.format(topic=topic),
            expected_output="A strong opening argument",
            agent=con_agent
        )
    )
    print("===== PRO:\n", con_opening, "\n")
    time.sleep(1)

    # PRO Rebuttal
    print("=" * 25)
    print("===== ROUND 2: REBUTTAL\n")
    print("=" * 25)
    print("===== PRO REBUTTAL is thinking...\n")
    pro_rebuttal = pro_agent.execute_task(
        Task(
            description=pro_rebuttal_prompt.format(topic=topic)
                        + f"\nOpponent said: \n{con_opening}",
            expected_output="A strong rebuttal argument",
            agent=pro_agent
        )
    )
    print("===== PRO REBUTTAL:\n", pro_rebuttal, "\n")
    time.sleep(1)

    # CON Rebuttal
    print("===== CON REBUTTAL is thinking...\n")
    con_rebuttal = con_agent.execute_task(
        Task(
            description=con_rebuttal_prompt.format(topic=topic)
                        + f"\nOpponent said: \n{pro_opening}",
            expected_output="A strong rebuttal argument",
            agent=con_agent
        )
    )
    print("===== CON REBUTTAL:\n", con_rebuttal, "\n")
    time.sleep(1)

    # HOST Summary
    print("=" * 25)
    print("===== CONCLUSION\n")
    print("=" * 25)
    print("===== HOST is concluding...\n")
    host_conclusion = host_agent.execute_task(
        Task(
            description=
            host_final_prompt.format(topic=topic)
            + f"\n\nPro Opening:\n{pro_opening}"
            + f"\n\nCon Opening:\n{con_opening}"
            + f"\n\nPro Rebuttal:\n{pro_rebuttal}"
            + f"\n\nCon Rebuttal:\n{con_rebuttal}",
            expected_output="A balanced final debate summary",
            agent=host_agent
        )
    )
    print("===== HOST FINAL:\n", host_conclusion, "\n")
    time.sleep(1)

    return DebateOutput(
        host_intro=str(host_intro),
        pro_opening=str(pro_opening),
        con_opening=str(con_opening),
        pro_rebuttal=str(pro_rebuttal),
        con_rebuttal=str(con_rebuttal),
        host_conclusion=str(host_conclusion),
    )