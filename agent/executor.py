from tools.basic_tools import study_tool, practice_tool

def execute_step(step: str):
    """
    Executor decides:
    - Which tool to use
    - Executes the step
    """
    if "practice" in step.lower():
        return practice_tool(step)
    return study_tool(step)