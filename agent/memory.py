def update_memory(state, observation):
    """
    Stores the result of each action.
    This memory helps the agent:
    - Track progress
    - Reflect later
    """
    state.memory.append(observation)