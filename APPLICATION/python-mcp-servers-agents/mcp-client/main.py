import asyncio
import json
import logging

from config import ApplicationConfig
from service import McpService

import logging

async def runApp():
    logging.info("Main execution started.")
    appConfig = ApplicationConfig()
    mcpService = McpService(appConfig)
    serverTools = await mcpService.connect_to_servers()

    for server_name, tools in serverTools.items():
        logging.info(f"=== Tools available on '{server_name}' ({len(tools)}) ===")
        for tool in tools:
            description = getattr(tool, "description", "") or ""
            logging.info(f" - {tool.name}: {description}")

    await interactiveLoop(mcpService, serverTools)

    logging.info("Main execution finished.")


async def interactiveLoop(mcpService: McpService, serverTools: dict[str, list]):
    """Prompt the user for a server / tool / arguments and invoke it."""
    # Drop servers that exposed no tools (failed connections).
    available = {name: tools for name, tools in serverTools.items() if tools}
    if not available:
        logging.warning("No servers with tools are available. Exiting interactive loop.")
        return

    server_names = list(available.keys())

    while True:
        print("\nAvailable servers:")
        for idx, name in enumerate(server_names, start=1):
            print(f" [{idx}] {name}")
        print(" [q] quit")
        choice = input("Select a server: ").strip()
        if choice.lower() in ("q", "quit", "exit"):
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(server_names)):
            print("Invalid selection.")
            continue
        server_name = server_names[int(choice) - 1]

        tools = available[server_name]
        print(f"\nTools on '{server_name}':")
        for idx, tool in enumerate(tools, start=1):
            desc = getattr(tool, "description", "") or ""
            print(f" [{idx}] {tool.name} - {desc}")
        print(" [b] back")
        tchoice = input("Select a tool: ").strip()
        if tchoice.lower() in ("b", "back"):
            continue
        if not tchoice.isdigit() or not (1 <= int(tchoice) <= len(tools)):
            print("Invalid selection.")
            continue
        tool = tools[int(tchoice) - 1]

        schema = getattr(tool, "inputSchema", None)
        if schema:
            print(f"Input schema: {json.dumps(schema, indent=2)}")
        raw = input("Arguments as JSON (or blank for none): ").strip()
        
        # Reconstructed completion for the cut-off try block at the bottom
        arguments = {}
        if raw:
            try:
                arguments = json.loads(raw)
            except json.JSONDecodeError:
                print("Invalid JSON format. Please try again.")
                continue

        try:
            print(f"Executing {tool.name}...")
            result = await mcpService.call_tool(server_name, tool.name, arguments)
            print(f"Result:\n{result}")
        except Exception as e:
            print(f"Error executing tool: {e}")


    
def printResult(result) -> None:
    """Pretty-print a fastmcp CallToolResult."""
    if getattr(result, "is_error", False):
        print(f"\n[ERROR] {result}\n")
        return

    data = getattr(result, "data", None)
    if data is not None:
        print(f"\nResult: {data}\n")
        return

    for item in getattr(result, "content", []) or []:
        text = getattr(item, "text", None)
        if text is not None:  # Extracted exactly as shown in screenshot typo
            print(f"\nResult: {text}\n")
            return

    print(f"\nResult: {result}\n")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    asyncio.run(runApp())