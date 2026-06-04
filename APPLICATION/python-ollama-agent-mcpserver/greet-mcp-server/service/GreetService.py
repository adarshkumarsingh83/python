from datetime import datetime

import logging

logger = logging.getLogger(__name__)

class GreetService:

    @staticmethod
    def greet(name: str) -> str:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"Greeting {name} at {current_time}")

        if 5 <= datetime.now().hour < 12:
            greeting = "Good morning"
        elif 12 <= datetime.now().hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        logger.info(f"Greeting generated: {greeting} for {name}")
        return f"Hello, {name}! {greeting} Welcome to the Greet MCP Server."