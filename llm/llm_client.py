import os

def call_llm(prompt: str) -> str:
    """
    Replace this with genAI LLM model currently mock this into a fixed response.

    IMPORTANT:
    - Right now this is mocked.
    - Later you can replace this with:
        - OpenAI API
        - Ollama (local LLaMA)
        - HuggingFace models
    
    @Input:
        prompt: Query to LLM model.
    @Output:
        Generated plan in textual format.
    
    """
    return """
    1. Understand PySpark basics and RDDs
    2. Learn joins, partitioning, and shuffles
    3. Practice PySpark transformations and actions
    4. Study performance tuning and caching
    5. Solve interview-level PySpark problems
    """