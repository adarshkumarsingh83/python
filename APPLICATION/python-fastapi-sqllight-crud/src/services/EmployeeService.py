from src.entity.Employee import Employee
from src.respository.EmployeeRepository import EmployeeRepository

class EmployeeService:
    
    def __init__(self, employeeRepository: EmployeeRepository):
        self.employeeRepository = employeeRepository
        
    def getEmployeeById(self, employeeId: int) -> Employee:
        return self.employeeRepository.getEmployeeById(employeeId)
    
    def getAllEmployees(self) -> list[Employee]:
        return self.employeeRepository.getAllEmployees()
    
    def addEmployee(self, employee: Employee) -> str:
        self.employeeRepository.addEmployee(employee)
        return f"{employee.name} added successfully"
    
    def updateEmployee(self, employeeId: int, employee: Employee) -> str:
        if self.employeeRepository.getEmployeeById(employeeId):
            self.employeeRepository.updateEmployee(employeeId, employee)
            return f"{employee.name} updated successfully"
        else:
            return f"Employee with ID {employeeId} not found"
        
    def deleteEmployee(self, employeeId: int) -> str:
        if self.employeeRepository.getEmployeeById(employeeId):
            self.employeeRepository.deleteEmployee(employeeId)
            return f"Employee with ID {employeeId} deleted successfully"
        else:
            return f"Employee with ID {employeeId} not found"
    