import config.AppConfig as appConfig
from datetime import datetime
from starlette.requests import Request
from starlette.responses import PlainTextResponse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
mcp = appConfig.getMcp()

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

@mcp.tool(name="greet", description="Greets the user with a message.")
def greet(name: str) -> str:
    print(f"Greeting user: {name}")
    # Get current hour
    hour = datetime.now().hour
    # Greeting based on time
    if hour < 12:
        message =f"Hello, {name}! Welcome to the MCP server. Good Morning, {name}!"
    elif hour < 17:
        message = f"Hello, {name}! Welcome to the MCP server. Good Afternoon, {name}!"
    else:
        message = f"Hello, {name}! Welcome to the MCP server. Good Evening, {name}!"
    return message