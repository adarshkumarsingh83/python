from service import GreetService
from config import McpConfig

import logging

logger = logging.getLogger(__name__)
mcpServer = McpConfig.getMcpServer()

def initializeGreetTool():
    logger.info("Initializing Greet Tool...")
    logger.info("Greet Tool initialized successfully.")

@mcpServer.tool(name="greet", description="Greet a user with a personalized message.")
def greet(name: str) -> str:
    logger.info(f"Processing greet request for {name}")
    msg =  GreetService.greet(name)
    logger.info(f"Generated greet message for {name}: {msg}")
    return msg
