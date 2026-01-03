from llm.llm_client import call_llm
from utils.parser import parse_steps

def plan_steps(goal: str):
    """
    Planner role:
    - Takes a high-level goal
    - Uses LLM reasoning
    - Produces a step-by-step plan
    """
    prompt = f"""
                You are a planning agent.
                Break the goal into actionable steps.

                Goal: {goal}
              """
    response = call_llm(prompt)
    return parse_steps(response)