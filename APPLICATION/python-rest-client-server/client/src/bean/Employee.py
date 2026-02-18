from pydantic import BaseModel

class Employee(BaseModel):
    employeeId: int
    name: str
    
    def __str__(self):
        return f"Employee ID: {self.employeeId}, Name: {self.name}"