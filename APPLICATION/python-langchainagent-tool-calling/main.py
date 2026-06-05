from langchain_classic import hub
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate
import json

try:
    from langchain_ollama import OllamaLLM as Ollama
except ImportError:
    from langchain_community.llms import Ollama


# 1. Initialize your local Ollama model
llm = Ollama(model="llama3")


# 2. Define custom tools for your agent
@tool
def calculate_area(input_str: str) -> str:
    """Calculate the area of a rectangle. Input can be 'length=15, width=20' or '{"length": 15, "width": 20}'"""
    try:
        # Try JSON format first
        if input_str.strip().startswith("{"):
            data = json.loads(input_str.strip())
            length = int(data.get("length", 0))
            width = int(data.get("width", 0))
        else:
            # Parse key=value format
            length = 0
            width = 0
            for part in input_str.split(","):
                if "=" in part:
                    key, val = part.strip().split("=")
                    if key.strip().lower() == "length":
                        length = int(val.strip())
                    elif key.strip().lower() == "width":
                        width = int(val.strip())
        return str(length * width)
    except Exception as e:
        return f"Error calculating area: {str(e)}"


@tool
def get_current_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return f"The weather in {location} is sunny and 72°F."


def executeMain():
    tools = [calculate_area, get_current_weather]

    # 3. Create a standard ReAct prompt template
    template = '''Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action (e.g., "length=15, width=20" for calculate_area, or "New York" for get_current_weather)
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}'''
    
    prompt = PromptTemplate(
        input_variables=["input", "agent_scratchpad"],
        template=template
    )

    # 4. Construct the agent and executor
    agent = create_react_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=False,
        max_iterations=10
    )

    # 5. Run the agent
    response = agent_executor.invoke({
        "input": "What is the area of a room that is 15 feet by 20 feet?"
    })
    print("Final Output:", response["output"])

    response = agent_executor.invoke({
        "input": "What is the current weather in New York City?"
    })
    print("Final Output:", response["output"])


if __name__ == "__main__":
    executeMain()