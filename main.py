from agent.state import AgentState
from agent.agent_loop import run_agent

if __name__ == "__main__":
    
    
    # Define agent goal
    goal = "Prepare for pyspark interview in 7 days"
    
    # Initialize agent state
    state = AgentState(goal)

    # Run agent loop
    final_state = run_agent(state)

    print("Plan")
    for step in final_state.plan:
        print("-", step)
    
    print("Memory")
    for mem in final_state.memory:
        print("-", mem)