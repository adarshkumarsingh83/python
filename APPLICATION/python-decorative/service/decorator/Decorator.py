import time
import random

def runFunctionInstance(func): 
    def runFunction(self,*args,**kwargs)-> int: 
        print(f"--- Something before {func.__name__} ---")
        startTime = time.time()
        func(self,*args,**kwargs)
        endTime = time.time()
        print(f"Total execution time: {endTime - startTime} seconds")
        print(f"--- Something after {func.__name__} ---")
        return 1
    return runFunction