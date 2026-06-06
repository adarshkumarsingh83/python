import logging
import datetime

class GreetService:
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("GreetService initialized")

    def greetAtLogin(self, name):
        self.logger.info(f"Greeting {name}")
        now = datetime.datetime.now()
        if now.hour < 12:
            return f"Good morning, {name}! How can I assist you today?"
        elif now.hour < 17:
            return f"Good afternoon, {name}! How can I assist you today?"
        else:
            return f"Good evening, {name}! How can I assist you today?"
        
    def greetAtLogout(self, name):
        self.logger.info(f"Greeting {name}")
        now = datetime.datetime.now()
        if now.hour < 12:
            return f"{name}, have a great day! Goodbye!"
        elif now.hour < 17:
            return f" {name}, have a great afternoon! Goodbye!"
        else:
            return f"{name}, have a great evening! Goodbye!"