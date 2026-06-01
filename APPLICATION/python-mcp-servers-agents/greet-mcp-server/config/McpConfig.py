from fastmcp import FastMCP
import logging 

class McpConfig:
    __logging = logging.getLogger(__name__)
    __mcpServer = FastMCP(name="MCP Server",version="1.0.0")

    @staticmethod
    def getMcpServer():
        McpConfig.__logging.info("Retrieving MCP Server instance...")
        return McpConfig.__mcpServer