from config import McpConfig
from tools import CalculationTool
import logging 
import os

mcpServer = McpConfig.getMcpServer()
logger = logging.getLogger(__name__)
CalculationTool.initializeMcpServer()

def startGreetMcpServer():
    logger.info("Starting Greet MCP Server...")
    port = int(os.getenv("MCP_SERVER_PORT", 6000))
    logger.info(f"Mcp Server started on  port: {port}")
    mcpServer.run(transport="sse", port=port)
    logger.info("Greet MCP Server started successfully.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("Initializing Greet MCP Server...")
    startGreetMcpServer()