from config import ApplicationConfig
from fastmcp import Client
from fastmcp.exceptions import ToolError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class McpService:

    def __init__(self, config: ApplicationConfig):
        self.config = config
        self.mcpServersConfig = self.config.mcp_servers_config()

        self.servers = self.config.mcp_servers()
        for name, details in self.servers.items():
            url = details.get("url")
            transport = details.get("transport")
            logger.info(
                f"Listening to MCP server '{name}' at {url} using {transport}"
            )

    async def call_tool(
        self,
        server_name: str,
        tool_name: str,
        arguments: dict | None = None,
    ):
        """Call a tool on the given server and return the result."""
        if server_name not in self.servers:
            raise KeyError(f"Unknown server: {server_name}")
        url = self.servers[server_name].get("url")
        logger.info(
            f"Calling tool '{tool_name}' on server '{server_name}' "
            f"with arguments={arguments or {}}"
        )
        try:
            async with Client(url) as client:
                return await client.call_tool(tool_name, arguments or {})
        except ToolError as exc:
            logger.warning(
                f"Tool '{tool_name}' on server '{server_name}' failed: {exc}"
            )
            return {"error": f"Tool '{tool_name}' failed: {exc}"}
        except Exception as exc:
            logger.error(
                f"Unexpected error calling tool '{tool_name}' on server "
                f"'{server_name}': {exc}"
            )
            return {"error": f"Tool '{tool_name}' could not be executed: {exc}"}

    async def get_tool_details(self) -> dict:
        """Get the details of a tool from the configuration."""
        logger.info("Getting tool details from configuration.")
        self.server_details = await self.config.get_server_tools_detatils()
        return self.server_details