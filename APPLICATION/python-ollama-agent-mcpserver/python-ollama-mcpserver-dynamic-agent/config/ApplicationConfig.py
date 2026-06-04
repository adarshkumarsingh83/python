import os
import logging
import asyncio
from pathlib import Path
from fastmcp import Client
from .ConfigReader import ConfigReader

logger = logging.getLogger(__name__)

# Project root = parent of this `config` package directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "resources" / "mcp-server.json"


class ApplicationConfig:
    """Application configuration loaded from a JSON file."""

    def __init__(self, config_path: str | Path | None = None) -> None:
        if config_path is None:
            env_path = os.getenv("APP_CONFIG_PATH")
            cfg_path = Path(env_path) if env_path else DEFAULT_CONFIG_PATH
        else:
            cfg_path = Path(config_path)

        # Resolve relative paths against the project root so the app works
        # regardless of the current working directory or OS.
        if not cfg_path.is_absolute():
            cfg_path = (PROJECT_ROOT / cfg_path).resolve()

        logger.info(f"Loading configuration from: {cfg_path}")
        self._reader = ConfigReader(cfg_path)

    def mcp_servers(self) -> dict[str, dict[str, str]]:
        """Return the individual MCP servers (`mcpServers`)."""
        return self._reader.get("mcp-list.mcpServers", {})

    def mcp_servers_config(self) -> dict[str, dict[str, dict[str, str]]]:
        """Return the full `mcp-list` configuration object."""
        return self._reader.get("mcp-list", {})

    async def connect_to_servers(self) -> dict[str, list]:
        """Connect to all configured MCP servers concurrently and list their tools.
        Returns a mapping of `server_name -> list_of_tools`.
        """
        servers = self.mcp_servers()
        logger.info(f"Connecting to MCP servers: {list(servers.keys())}")
        results = await asyncio.gather(
            *(
                self._connect_and_list_tools(name, details)
                for name, details in servers.items()
            ),
            return_exceptions=False,
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
                        f"  - {tool.name}: {getattr(tool, 'description', '') or ''}"
                    )
                return name, tools
        except Exception as exc:
            logger.error(f"Failed to connect to MCP server '{name}': {exc}")
            return name, []

    async def get_server_tools_detatils(self) -> list[dict]:
        """Get details of all tools from all servers in a structured format."""
        serverTools = await self.connect_to_servers()
        tools_details_list = []
        for server_name, tools in serverTools.items():
            server_info = self.mcp_servers().get(server_name, {})
            for tool in tools:
                tools_details_list.append({
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description or "",
                        "parameters": getattr(tool, "inputSchema", None) or {},
                        "serverName": server_name,
                        "url": server_info.get("url"),
                        "transport": server_info.get("transport"),
                    },
                })

        logger.info(
            "Retrieved tool details from all servers. '{tools_count}' tools found.".format(
                tools_count=len(tools_details_list)
            )
        )
        return tools_details_list