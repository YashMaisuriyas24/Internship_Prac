from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import SummarizationMiddleware

@tool
def search_database(query: str, limit: int = 10) -> str:
    """Search the customer database for records matching the query.

    Args:
        query: Search terms to look for
        limit: Maximum number of results to return
    """
    return f"Found {limit} results for '{query}'"

checkpointer  = InMemorySaver()

agent = create_agent(
    model="llama3.2:latest",
    tools=[search_database],
    middleware=[
        SummarizationMiddleware(
            model="llama3.2:latest"
        )
    ],
    checkpointer=InMemorySaver(),
)


agent.invoke(
    {"messages": [{"role": "user", "content": "Hi! My name is Bob."}]},
    {"configurable": {"thread_id": "1"}},
)