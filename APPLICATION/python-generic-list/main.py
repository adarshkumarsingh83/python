from processor.DataProcessor import DataProcessor
from bean.Employee import Employee

def mainExecutor() -> None:
    print(f'\n')
    stringList: list[str] = ["Hello", "World", "Python", "Generics"]
    dataProcessor: DataProcessor = DataProcessor[str]()
    responseItems : list[str] = dataProcessor.processData(stringList)
    for item in responseItems:
        print(f'response {item}')
        
    print(f'\n')
    integerList: list[int] = [1, 2, 3, 4, 5]
    dataProcessor: DataProcessor = DataProcessor[int]()
    responseItems : list[int] = dataProcessor.processData(integerList)
    for item in responseItems:
        print(f'response {item}')
    
    print(f'\n')
    dataProcessor: DataProcessor = DataProcessor[Employee]()
    employeeList = [
        Employee("E001", "Alice"),
        Employee("E002", "Bob"),
        Employee("E003", "Charlie"),
        Employee("E004", "Diana")
    ]
    responseItems : list[Employee] = dataProcessor.processData(employeeList)
    for item in responseItems:
        print(item)
        
    
if __name__ == "__main__":
    mainExecutor()