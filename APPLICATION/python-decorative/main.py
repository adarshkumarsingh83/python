from service.ServiceOne import ServiceOne
from service.ServiceTwo import ServiceTwo


def main():
    
    serviceOne = ServiceOne("MyServiceOne")
    runFunction = serviceOne.runFunctionInstance(serviceOne.start, serviceOne.performTaskOne, serviceOne.stop)
    runFunction("MyServiceOne->performTaskOne")
    
    serviceTwo = ServiceTwo("MyServiceTwo")
    serviceTwo.performTaskTwo("MyServiceTwo->performTaskTwo")
    
    
if __name__ == "__main__":
    main()
    
    