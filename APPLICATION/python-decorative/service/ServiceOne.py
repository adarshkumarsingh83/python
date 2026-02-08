import time
import random

class ServiceOne:
    
    def __init__(self, name: str) -> None:
        self.name = name

    def start(self) -> int:
        print(f"{self.name} is starting...")
        return 1
        
    def performTaskOne(self,name: str) -> int:
        print(f"{self.name} is performing a task...")
        random_integer = random.randint(1, 10)
        time.sleep(random_integer)
        return 1
        
    def stop(self) -> int:
        print(f"{self.name} is stopping...")
        return 1
        
    def runFunctionInstance(self, startFunction, performFunction, stopFunction): 
        def runFunction(self,*args, **kwargs):
            startTime = time.time();
            startFunction()
            performFunction(self,*args,**kwargs)
            stopFunction()
            endTime = time.time();
            print(f"Total execution time: {endTime - startTime} seconds")
        return runFunction