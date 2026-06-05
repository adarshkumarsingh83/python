import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain_community")

from langchain_community.tools import DuckDuckGoSearchResults, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import create_agent
from langchain_ollama import ChatOllama


def main():
    llm = ChatOllama(
        model="llama3.1:latest",
        temperature=0,
    )

    search = DuckDuckGoSearchResults()
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    tools = [search, wikipedia]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are a helpful assistant. Based on user query, look for information "
            "using DuckDuckGo Search and Wikipedia and then give the final answer"
        ),
    )

    result = agent.invoke({
        "messages": [(
            "human",
            "How is Ollama used for running LLM locally?",
        )]
    })

    # Print the final assistant message
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
