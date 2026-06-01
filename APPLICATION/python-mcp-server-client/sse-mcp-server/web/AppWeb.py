import logging
import config.AppConfig as AppConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = AppConfig.getMcp()

@mcp.tool(name="add_numbers", description="Adds two numbers together.")
def add_numbers(a: int, b: int) -> str:
    """Adds two numbers together."""
    logging.info(f"add_numbers request to add {a} and {b}")
    result = a + b
    logger.info(f"Adding {a} and {b} to get {result}")
    return str(result)


@mcp.tool(name="subtract_numbers", description="Subtracts the second number from the first.")
def subtract_numbers(a: int, b: int) -> str:
    """Subtracts the second number from the first."""
    logging.info(f"subtract_numbers request to subtract {b} from {a}")
    result = a - b
    logger.info(f"Subtracting {b} from {a} to get {result}")
    return str(result)

@mcp.tool(name="multiply_numbers", description="Multiplies two numbers together.")
def multiply_numbers(a: int, b: int) -> str:
    """Multiplies two numbers together."""
    logging.info(f"multiply_numbers request to multiply {a} and {b}")
    result = a * b
    logger.info(f"Multiplying {a} and {b} to get {result}")
    return str(result)

@mcp.tool(name="divide_numbers", description="Divides the first number by the second.")
def divide_numbers(a: int, b: int) -> str:
    """Divides the first number by the second."""
    logging.info(f"divide_numbers request to divide {a} by {b}")
    if b == 0:
        logger.warning("Attempted to divide by zero")
        return "Error: Cannot divide by zero."
    result = a / b
    logger.info(f"Dividing {a} by {b} to get {result}")
    return str(result)

@mcp.tool(name="compare_numbers", description="Compares two numbers and returns which one is greater.")
def compare_numbers(a: int, b: int) -> str:
    """Compares two numbers and returns which one is greater."""
    logging.info(f"compare_numbers request to compare {a} and {b}")
    if a > b:
        result = f"{a} is greater than {b}."
    elif a < b:
        result = f"{b} is greater than {a}."
    else:
        result = "Both numbers are equal."
    logger.info(f"Comparison result: {result}")
    return result