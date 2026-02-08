import time
import random
from service.decorator.Decorator import runFunctionInstance

class ServiceThree:
    
    def __init__(self, name: str) -> None:
        self.name = name
        
    def start(self) -> int:
        print(f"{self.name} is starting...")
        return 1

    @runFunctionInstance
    def performTaskThree(self,name: str) -> int:
        self.start()
        print(f"{self.name} is performing a task...")
        random_integer = random.randint(1, 10)
        time.sleep(random_integer)
        print(f"{self.name} is performed a task...")
        self.stop()
        return 1
    
    @runFunctionInstance
    def performNewTask(self) -> int:
        self.start()
        print(f"{self.name} is performing a new task...")
        random_integer = random.randint(1, 10)
        time.sleep(random_integer)
        print(f"{self.name} is performed a new task...")
        self.stop()
        return 1
    
    def stop(self) -> int:
        print(f"{self.name} is stopping...")
        return 1
    

        
