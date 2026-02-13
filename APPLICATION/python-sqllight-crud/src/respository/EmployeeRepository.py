import sqlite3
from src.config.persistance.DbConection import DbConnection

class EmployeeRepository:
    def __init__(self, dbConnection: DbConnection):
        self.dbConnection = dbConnection

    def createEmployeeTable(self, name: str) -> str:
        connection: sqlite3.Connection = self.dbConnection.getDBConnection()
        cursor: sqlite3.Cursor = self.dbConnection.getDBCursor()
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
            cursor.execute("INSERT INTO employee (name) VALUES (?)", (name))
            connection.commit()
            return "Employee table created and employee added successfully."
        except Exception as e:
            print(f"Error creating employee: {e}")
            return "Error creating employee."
        
    def addEmployee(self, name: str) -> str:
        connection: sqlite3.Connection = self.dbConnection.getDBConnection()
        cursor: sqlite3.Cursor = self.dbConnection.getDBCursor()
        try:
            cursor.execute("INSERT INTO employee (name) VALUES (?)", (name,))
            connection.commit()
            return "Employee added successfully."
        except Exception as e:
            print(f"Error adding employee: {e}")
            return "Error adding employee."
        
    def getEmployeeById(self, empId: int) -> dict:
        connection: sqlite3.Connection = self.dbConnection.getDBConnection()
        cursor: sqlite3.Cursor = self.dbConnection.getDBCursor()
        try:
            cursor.execute("SELECT id, name FROM employee WHERE id = ?", (empId,))
            row = cursor.fetchone()
            if row:
                return {"id": row[0], "name": row[1]}
            else:
                return None
        except Exception as e:
            print(f"Error fetching employee by id: {e}")
            return None
        
    def getAllEmployees(self) -> list:
        connection: sqlite3.Connection = self.dbConnection.getDBConnection()
        cursor: sqlite3.Cursor = self.dbConnection.getDBCursor()
        try:
            cursor.execute("SELECT id, name FROM employee")
            rows = cursor.fetchall()
            return [{"id": row[0], "name": row[1]} for row in rows]
        except Exception as e:
            print(f"Error fetching all employees: {e}")
            return []
        
    def updateEmployee(self, empId: int, name: str) -> str:
        connection: sqlite3.Connection = self.dbConnection.getDBConnection()
        cursor: sqlite3.Cursor = self.dbConnection.getDBCursor()
        try:
            cursor.execute("UPDATE employee SET name = ? WHERE id = ?", (name, empId))
            connection.commit()
            return "Employee updated successfully." if cursor.rowcount > 0 else "Employee not found."
        except Exception as e:
            print(f"Error updating employee: {e}")
            return "Error updating employee."
        
    def deleteEmployee(self, empId: int) -> str:
        connection: sqlite3.Connection = self.dbConnection.getDBConnection()
        cursor: sqlite3.Cursor = self.dbConnection.getDBCursor()
        try:
            cursor.execute("DELETE FROM employee WHERE id = ?", (empId,))
            connection.commit()
            return "Employee deleted successfully." if cursor.rowcount > 0 else "Employee not found."
        except Exception as e:
            print(f"Error deleting employee: {e}")
            return "Error deleting employee."