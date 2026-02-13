from src.config.ApplicationConfig import ApplicationConfig

def executeMain():
    print("Starting application...")
    appConfig = ApplicationConfig()
    print("Application configuration loaded successfully.")
    print()
    employeeRepo = appConfig.getEmployeeRepository()
    print(employeeRepo.getAllEmployees())
    employeeRepo.addEmployee("John Doe")
    print(employeeRepo.getAllEmployees())
    employeeRepo.updateEmployee(1, "Adarsh KUmar singh ")
    print(employeeRepo.getAllEmployees())
    employeeRepo.deleteEmployee(1)
    print(employeeRepo.getAllEmployees())
    


if __name__ == "__main__":
    executeMain()