import time
import random

def runFunctionInstance(performTaskTwo): 
    def runFunction(self,*args,**kwargs)-> int: 
        startTime = time.time()
        performTaskTwo(self,*args,**kwargs)
        endTime = time.time()
        print(f"Total execution time: {endTime - startTime} seconds")
        return 1
    return runFunction