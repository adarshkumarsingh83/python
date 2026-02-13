from service.EmployeeService import EmployeeService
from fastapi import APIRouter
from bean.Employee import Employee

class ApplicationRouter:
    
    def __init__(self):
        self.router = APIRouter()
        self.service: EmployeeService = EmployeeService()
        self.router.add_api_route("/api/router/employee/{employeeId}", self.get_employee, methods=["GET"])
        self.router.add_api_route("/api/router/employees", self.get_all_employees, methods=["GET"])
        self.router.add_api_route("/api/router/employee", self.add_employee, methods=["POST"])
        self.router.add_api_route("/api/router/employee/{employeeId}", self.update_employee, methods=["PUT"])
        self.router.add_api_route("/api/router/employee/{employeeId}", self.delete_employee, methods=["DELETE"])
        
        
    def getRouter(self) -> APIRouter:
        return self.router
    
    def get_employee(self,employeeId: int) -> Employee:
        return self.service.getEmployeeById(employeeId)
    
    def get_all_employees(self)-> list[Employee]:
        return self.service.getAllEmployees()
    
    def add_employee(self,employee: Employee) -> str:
        return self.service.addEmployee(employee)
    
    def update_employee(self,employeeId: int, employee: Employee) -> str:
        return self.service.updateEmployee(employeeId, employee)
    
    def delete_employee(self,employeeId: int) -> str:
        return self.service.deleteEmployee(employeeId)