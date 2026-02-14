
import uvicorn
from fastapi import FastAPI
from src.config.ApplicationConfig import ApplicationConfig
from src.router.ApplicationRouter import ApplicationRouter
from src.entity.Employee import Employee

def executeMain():
    print("Starting application...")
    appConfig = ApplicationConfig()
    print("Application configuration loaded successfully.")
    print()
    employeeRepo = appConfig.getEmployeeRepository()
    print(employeeRepo.getAllEmployees())
    employeeRepo.addEmployee(Employee(employeeId=0, name="John Doe"))
    print(employeeRepo.getAllEmployees())
    employeeRepo.updateEmployee(1, Employee(employeeId=1, name="Adarsh Kumar Singh"))
    print(employeeRepo.getAllEmployees())
    employeeRepo.deleteEmployee(1)
    print(employeeRepo.getAllEmployees())
    

def executeWeb():
    print("Starting web application...")
    appConfig = ApplicationConfig()
    print("Application configuration loaded successfully.")
    app = FastAPI()
    app.router.include_router(prefix="/v",router=appConfig.getApplicationRouter().getRouter())
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    
if __name__ == "__main__":
    executeWeb()