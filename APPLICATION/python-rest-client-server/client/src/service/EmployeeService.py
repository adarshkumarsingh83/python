from src.bean.Employee import Employee
from src.service.IntegrationService import IntegrationService

class EmployeeService:
    
    def __init__(self, integrationService: IntegrationService):
        self.integrationService = integrationService
        
    def getEmployeeById(self, employeeId: int) -> Employee:
        emp_data = self.integrationService.getEmployee(employeeId)
        return Employee(**emp_data) if emp_data else None
    
    def getAllEmployees(self) -> list[Employee]:
        employees_data = self.integrationService.getAllEmployees()
        return [Employee(**emp_data) for emp_data in employees_data]
    
    def addEmployee(self, employee: Employee) -> str:
        self.integrationService.createEmployee(employee)
        return f"{employee.name} added successfully"
    
    def updateEmployee(self, employeeId: int, employee: Employee) -> str:
        self.integrationService.updateEmployee(employeeId, employee)
        return f"{employee.name} updated successfully"
    
    def deleteEmployee(self, employeeId: int) -> str:
        self.integrationService.deleteEmployee(employeeId)
        return f"Employee with ID {employeeId} deleted successfully"
    