from config import AppMcpConfig
from tools import DataTools
from service import InitDataService
import logging
import os

logger = logging.getLogger(__name__)
mcpServer = AppMcpConfig.get_mcp_server()

def executeDataServer():
    logger.info("Starting DataServer...")
    InitDataService.initialize_data()
    port = int(os.getenv("MCP_SERVER_PORT", 7000))
    logger.info(f"Mcp Server started on  port: {port}")
    mcpServer.run(transport="sse", port=port)
    logger.info("Greet MCP Server started successfully.")


if __name__ == "__main__":
    executeDataServer()