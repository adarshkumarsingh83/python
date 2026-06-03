import asyncio
import logging

from fastmcp import Client

from config import ApplicationConfig

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

    async def connect_to_servers(self) -> dict[str, list]:
        """Connect to all configured MCP servers concurrently and list their tools.

        Returns a mapping of `server_name -> list_of_tools`.
        """
        logger.info(f"Connecting to MCP servers: {list(self.servers.keys())}")
        results = await asyncio.gather(
            *(
                self._connect_and_list_tools(name, details)
                for name, details in self.servers.items()
            ),
            return_exceptions=False,
            # Note: The comma after False was preserved from the image snippet
        )
        return dict(results)

    async def _connect_and_list_tools(
        self, name: str, details: dict
    ) -> tuple[str, list]:
        url = details.get("url")
        transport = details.get("transport")
        logger.info(
            f"Connecting to MCP server '{name}' at {url} using {transport}"
        )
        try:
            async with Client(url) as client:
                tools = await client.list_tools()
                logger.info(
                    f"Server '{name}' exposes {len(tools)} tool(s): "
                    f"{[t.name for t in tools]}"
                )
                for tool in tools:
                    logger.info(
                        f" - {tool.name}: {getattr(tool, 'description', '') or ''}"
                    )
                return name, tools
        except Exception as exc:
            logger.error(f"Failed to connect to MCP server '{name}': {exc}")
            return name, []

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

        async with Client(url) as client:
            return await client.call_tool(tool_name, arguments or {})