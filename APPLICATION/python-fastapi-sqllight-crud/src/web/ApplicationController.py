from fastapi import FastAPI
from src.entity.Employee import Employee
from src.services.EmployeeService import EmployeeService

class ApplicationController:
    
    app = FastAPI()
    
    def __init__(self):
        self.employeeService: EmployeeService = EmployeeService()
        
        
    @app.get("/api/controller/employee/{employeeId}")
    def get_employee(self,employeeId: int) -> Employee:
        return self.employeeService.getEmployeeById(employeeId)
    
    @app.get("/api/controller/employees")
    def get_all_employees(self,) -> list[Employee]:
        return self.employeeService.getAllEmployees()
    
    @app.post("/api/controller/employee")
    def add_employee(self,employee: Employee) -> str:
        return self.employeeService.addEmployee(employee)
    
    @app.put("/api/controller/employee/{employeeId}")
    def update_employee(self,employeeId: int, employee: Employee) -> str:
        return self.employeeService.updateEmployee(employeeId, employee)
    
    @app.delete("/api/controller/employee/{employeeId}")
    def delete_employee(self,employeeId: int) -> str:
        return self.employeeService.deleteEmployee(employeeId)