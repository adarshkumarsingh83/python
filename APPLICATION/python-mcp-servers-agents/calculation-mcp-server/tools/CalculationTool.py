from service import CalculationService
from config import McpConfig
import logging

mcpServer = McpConfig.getMcpServer()
logger = logging.getLogger(__name__)

def initializeMcpServer():
    logger.info("Initializing MCP Server with tools...")
    logger.info("MCP Server initialized with all tools.")

@mcpServer.tool(name="add_tool", description="Tool to add two numbers")
def add_tool(a: float, b: float):
    calculation_service = CalculationService()
    logger.info(f"add_tool called with {a} and {b}")
    return calculation_service.add(a, b)


@mcpServer.tool(name="subtract_tool", description="Tool to subtract two numbers")
def subtract_tool(a: float, b: float):
    calculation_service = CalculationService()
    logger.info(f"subtract_tool called with {a} and {b}")
    return calculation_service.subtract(a, b)

@mcpServer.tool(name="multiply_tool", description="Tool to multiply two numbers")
def multiply_tool(a: float, b: float):
    calculation_service = CalculationService()
    logger.info(f"multiply_tool called with {a} and {b}")
    return calculation_service.multiply(a, b)

@mcpServer.tool(name="divide_tool", description="Tool to divide two numbers")
def divide_tool(a: float, b: float):
    calculation_service = CalculationService()
    logger.info(f"divide_tool called with {a} and {b}")
    return calculation_service.divide(a, b)

@mcpServer.tool(name="compare_tool", description="Tool to compare two numbers and determine if one is bigger, smaller, or equal")
def compare_tool(a: float, b: float):
    calculation_service = CalculationService()
    logger.info(f"compare_tool called with {a} and {b}")
    return calculation_service.compare(a, b)

