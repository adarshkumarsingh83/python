import time
import random

class ServiceTwo:
    
    def __init__(self, name: str) -> None:
        self.name = name
        
    def runFunctionInstance(performTaskTwo): 
        def runFunction(self,*args,**kwargs)-> int: 
            startTime = time.time()
            performTaskTwo(self,*args,**kwargs)
            endTime = time.time()
            print(f"Total execution time: {endTime - startTime} seconds")
            return 1
        return runFunction
        
    def start(self) -> int:
        print(f"{self.name} is starting...")
        return 1

    @runFunctionInstance
    def performTaskTwo(self,name: str) -> int:
        self.start()
        print(f"{self.name} is performing a task...")
        random_integer = random.randint(1, 10)
        time.sleep(random_integer)
        print(f"{self.name} is performed a task...")
        self.stop()
        return 1
    
    def stop(self) -> int:
        print(f"{self.name} is stopping...")
        return 1
    

        
