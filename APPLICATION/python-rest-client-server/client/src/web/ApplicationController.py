from fastapi import FastAPI, Depends
from src.bean.Employee import Employee
from src.service.EmployeeService import EmployeeService


class ApplicationController:
    
    app = FastAPI()
    
    def __init__(self, employeeService: EmployeeService):
        self.employeeService: EmployeeService = employeeService
        
    @staticmethod 
    def getEmployeeService(self) -> EmployeeService:
        return self.employeeService

    @staticmethod   
    @app.get("/api/employees/{employeeId}")   
    def getEmployeeById( employeeId: int, service = Depends(getEmployeeService)) -> Employee:
        return service.getEmployeeById(employeeId)
    @staticmethod
    @app.get("/api/employees")
    def getAllEmployees(service = Depends(getEmployeeService)) -> list[Employee]:
        return service.getAllEmployees()
    @staticmethod
    @app.post("/api/employees")
    def addEmployee( employee: Employee, service = Depends(getEmployeeService)) -> str:
        return service.addEmployee(employee)
    @staticmethod
    @app.put("/api/employees/{employeeId}")
    def updateEmployee( employeeId: int, employee: Employee, service = Depends(getEmployeeService)) -> str:
        return service.updateEmployee(employeeId, employee)
    @staticmethod
    @app.delete("/api/employees/{employeeId}")
    def deleteEmployee( employeeId: int, service = Depends(getEmployeeService)) -> str:
        return service.deleteEmployee(employeeId)
    
    def getApp(self) -> FastAPI:
        return self.app