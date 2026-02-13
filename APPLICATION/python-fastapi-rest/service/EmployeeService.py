from bean.Employee import Employee

class EmployeeService:
    
    def __init__(self):
        self.employees = {
            1: Employee(employeeId=1, name="Adarsh kumar"),
            2: Employee(employeeId=2, name="Amit kumar"),
            3: Employee(employeeId=3, name="Sonu Singh")
        }
        
    def getEmployeeById(self, employeeId: int) -> Employee:
        return self.employees.get(employeeId)
    
    def getAllEmployees(self) -> list[Employee]:
        return list(self.employees.values())
    
    def addEmployee(self, employee: Employee) -> str:
        self.employees[employee.employeeId] = employee
        return f"{employee.name} added successfully"
    
    def updateEmployee(self, employeeId: int, employee: Employee) -> str:
        if employeeId in self.employees:
            self.employees[employeeId] = employee
            return f"{employee.name} updated successfully"
        else:
            return f"Employee with ID {employeeId} not found"
        
    def deleteEmployee(self, employeeId: int) -> str:
        if employeeId in self.employees:
            del self.employees[employeeId]
            return f"Employee with ID {employeeId} deleted successfully"
        else:
            return f"Employee with ID {employeeId} not found"
    