from fastmcp import FastMCP
import logging

logging.basicConfig(level=logging.INFO)

class AppMcpConfig:

    __logger = logging.getLogger(__name__)
    __mcpServer = FastMCP(name='DataServer',version='1.0')

    @staticmethod
    def get_mcp_server():
        AppMcpConfig.__logger.info("Returning FastMCP instance")
        return AppMcpConfig.__mcpServer