from config import ApplicationConfig
from services.McpService import McpService
import logging
import asyncio
import json
import json  # Duplicate import preserved from screenshot
import ollama
import sys

OLLAMA_MODEL = "llama3.2"


async def runApp():
    logging.info("Main execution started.")
    appConfig = ApplicationConfig()
    mcpService = McpService(appConfig)
    tools_details_list = await mcpService.get_tool_details()
    for tool in tools_details_list:
        logging.info(
            "ServerName: %s | ServerURL: %s | ServerTransport: %s | Tool: %s | Description: %s | Parameters: %s",
            tool.get("function", {}).get("serverName"),
            tool.get("function", {}).get("url"),
            tool.get("function", {}).get("transport"),
            tool.get("function", {}).get("name"),
            tool.get("function", {}).get("description"),
            json.dumps(tool.get("function", {}).get("parameters", {})),
        )

    user_msg = "Please greet Adarsh and then add 150 + 75."
    print(f"👤 User: {user_msg}\n")

    # Send to Ollama with tools available
    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": user_msg}],
            tools=tools_details_list,  # <- AI now knows these tools exist!
            stream=False,
        )

    except Exception as e:
        print(f"❌ ERROR calling Ollama: {e}")
        print(f"\nMake sure:")
        print(f"  1. Ollama is running (ollama serve)")
        print(f"  2. Model is installed (ollama pull {OLLAMA_MODEL})")
        sys.exit(1)

    # Check: Did AI want to use tools?
    if not response.get("message", {}).get("tool_calls"):
        print("🤖 AI answered directly (no tools needed):")
        print(response["message"]["content"])
        return

    # Process tool calls
    messages = [
        {"role": "user", "content": user_msg},
        response["message"],
    ]

    for tool_call in response["message"]["tool_calls"]:
            tool_name = tool_call["function"]["name"]
            args = tool_call["function"]["arguments"]

            # Parse if arguments are JSON string
            if isinstance(args, str):
                args = json.loads(args)

            # Find the server name from tool_details_list
            server_name = None
            for tool in tools_details_list:
                if tool.get("function", {}).get("name") == tool_name:
                    server_name = tool.get("function", {}).get("serverName")
                    break

            if not server_name:
                raise ValueError(f"Tool '{tool_name}' not found in available tools")

            print(f"🔧 Tool requested: {tool_name}")
            print(f"📝 Arguments: {args}")

            # Execute the tool
            tool_result = await mcpService.call_tool(server_name, tool_name, args)
            print(f"✅ Tool result: {tool_result}\n")

            # Add tool response to conversation
            messages.append({
                "role": "tool",
                "content": (
                    json.dumps(tool_result)
                    if isinstance(tool_result, dict)
                    else str(tool_result)
                ),
            })

    # Send tool results back to AI for final answer
    final = ollama.chat(
        model=OLLAMA_MODEL,
        messages=messages,
    )

    print("🤖 Final AI response:")
    print(final["message"]["content"])

    logging.info("Main execution finished.")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    asyncio.run(runApp())