import logging

logger = logging.getLogger(__name__)


class CalculationService:

    def __init__(self):
        logger.info("CalculationService initialized")

    def add(self, a, b):
        logger.info(f"Adding {a} and {b}")
        return a + b


    def subtract(self, a, b):
        logger.info(f"Subtracting {b} from {a}")
        return a - b


    def multiply(self, a, b):
        logger.info(f"Multiplying {a} and {b}")
        return a * b

    def divide(self, a, b):
        if b == 0:
            logger.error("Attempted to divide by zero")
            raise ValueError("Cannot divide by zero")
        logger.info(f"Dividing {a} by {b}")
        return a / b
    
    def compare(self, a, b):
        """Compare two numbers and return the relationship"""
        logger.info(f"Comparing {a} and {b}")
        if a > b:
            return {"result": "bigger", "message": f"{a} is bigger than {b}"}
        elif a < b:
            return {"result": "smaller", "message": f"{a} is smaller than {b}"}
        else:
            return {"result": "equal", "message": f"{a} is equal to {b}"}