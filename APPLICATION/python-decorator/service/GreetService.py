from datetime import datetime
from functools import wraps

class GreetService:
    
    def __init__(self):
        pass
    
    @staticmethod
    def greet_based_on_time() -> str:
        current_time = datetime.now().time()
        if current_time.hour < 12:
            return "Good morning"
        elif 12 <= current_time.hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
    
    @staticmethod
    def greet_with_time(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            greeting = GreetService.greet_based_on_time()
            kwargs['wish'] = greeting
            return function(*args, **kwargs)
        return wrapper
    
    @greet_with_time
    def greet(self, name: str, wish: str = None) -> str:
        return f"{name} {wish}!"