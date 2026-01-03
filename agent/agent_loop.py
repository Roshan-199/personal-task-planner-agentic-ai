from agent.planner import plan_steps
from agent.executor import execute_step
from agent.memory import update_memory

def run_agent(state):
    """
    This is the HEART of agentic AI.

    Loop:
    1. Plan
    2. Execute
    3. Observe
    4. Store memory
    5. Decide next step
    """
    
    # Step 1: Create plan from goal
    state.plan = plan_steps(state.goal)

    # Step 2: Execute each step
    for step in state.plan:
        state.current_step = step
        
        # Perform action
        result = execute_step(step)

        # Observe and remember
        update_memory(state, result)
        
        # Mark step as completed
        state.completed_steps.append(step)
    
    # Step 3: Mark agent as done
    state.done = True

    return state