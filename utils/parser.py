def parse_steps(llm_response: str):
    """
    Converts raw LLM output into a clean Python list.

    Example Input:
    1. Step one
    2. Step two

    Output:
    ["Step one", "Step two"]
    """
    steps = []
    for line in llm_response.split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            steps.append(line.split(".", 1)[1].strip())
    return steps