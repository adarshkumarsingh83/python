from service.ServiceOne import ServiceOne
from service.ServiceTwo import ServiceTwo
from service.ServiceThree import ServiceThree


def main():
    
    serviceOne = ServiceOne("MyServiceOne")
    runFunction = serviceOne.runFunctionInstance(serviceOne.start, serviceOne.performTaskOne, serviceOne.stop)
    runFunction("MyServiceOne->performTaskOne")
    
    serviceTwo = ServiceTwo("MyServiceTwo")
    serviceTwo.performTaskTwo("MyServiceTwo->performTaskTwo")
    
    serviceThree = ServiceThree("MyServiceThree")
    serviceThree.performTaskThree("MyServiceThree->performTaskThree")
    
    
if __name__ == "__main__":
    main()
    
    