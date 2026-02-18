# Python REST Client-Server Application

## Table of Contents
- [Project Overview](#project-overview)
- [Project Description](#project-description)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [API Usage Examples](#api-usage-examples)
- [Code Explanation](#code-explanation)
- [Troubleshooting](#troubleshooting)

---

## Project Overview

This is a **Python REST API Server Application** built with **FastAPI** that manages Employee data. It provides a complete RESTful web service with CRUD (Create, Read, Update, Delete) operations for managing employees. The application uses SQLite as the database and follows a layered architecture pattern with controllers, services, repositories, and entities.

**Application Name:** Espark Server Application

---

## Project Description

The Espark Server Application is a RESTful API designed to manage employee information. It demonstrates:

- **RESTful API Design**: Implements standard REST conventions for HTTP methods
- **Layered Architecture**: Separation of concerns with controller, service, and repository layers
- **Database Integration**: SQLite for persistent data storage
- **Configuration Management**: YAML and properties-based configuration
- **API Documentation**: Interactive Swagger UI for API exploration
- **Type Hints**: Python type annotations for better code quality

**Key Features:**
- Create new employees
- Retrieve employee details (single or all)
- Update employee information
- Delete employees
- Automatic API documentation with Swagger/OpenAPI

---

## Architecture

The application follows a **4-Layer Architecture Pattern**:

```
┌─────────────────────────────────────┐
│   Web Layer (Controllers)            │  ← HTTP Requests/Responses
├─────────────────────────────────────┤
│   Service Layer (Business Logic)     │  ← Business Rules & Validations
├─────────────────────────────────────┤
│   Repository Layer (Data Access)     │  ← Database Operations
├─────────────────────────────────────┤
│   Entity Layer (Data Models)         │  ← Data Structure Definitions
└─────────────────────────────────────┘
```

**Component Breakdown:**

1. **Entity Layer** (`src/entity/`)
   - Defines data models (Employee)
   - Uses Pydantic for data validation

2. **Repository Layer** (`src/respository/`)
   - Handles database CRUD operations
   - Manages SQLite connections
   - Abstraction for database operations

3. **Service Layer** (`src/services/`)
   - Contains business logic
   - Validates data
   - Orchestrates repository operations

4. **Web Layer** (`src/web/`)
   - HTTP endpoint definitions
   - Request/Response handling
   - Router configuration

5. **Configuration Layer** (`src/config/`)
   - Application initialization
   - Database connection setup
   - Configuration property loading (YAML, Properties)

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **Virtual Environment**: Python's venv module
- **SQLite3**: Usually comes with Python
- **Operating System**: Windows, macOS, or Linux

**Verify Installation:**

```bash
python --version
pip --version
sqlite3 --version
```

---

## Project Structure

```
server/
├── main.py                           # Application entry point
├── README.md                         # This file
├── env/                              # Virtual environment (created during setup)
│
├── resources/                        # Configuration and database files
│   ├── application.properties        # Properties configuration
│   ├── application.yml               # YAML configuration
│   └── db/
│       ├── scripts/
│       │   └── espark.sql           # Database initialization script
│       └── store/
│           └── espark.db            # SQLite database file (created at runtime)
│
└── src/                              # Source code
    ├── config/                       # Configuration Package
    │   ├── ApplicationConfig.py      # Main configuration loader
    │   ├── PropertiesReader.py       # Properties file reader
    │   ├── YamlReader.py             # YAML file reader
    │   ├── bean/
    │   │   └── ConfigurationBean.py  # Configuration data classes
    │   └── persistance/
    │       ├── DbConection.py        # Database connection manager
    │       └── InitializedDb.py      # Database initialization
    │
    ├── entity/                       # Data Models
    │   └── Employee.py               # Employee entity
    │
    ├── respository/                  # Data Access Layer
    │   └── EmployeeRepository.py     # Employee CRUD operations
    │
    ├── services/                     # Business Logic Layer
    │   └── EmployeeService.py        # Employee business logic
    │
    ├── router/                       # API Routing
    │   └── ApplicationRouter.py      # API route definitions
    │
    └── web/                          # Web/Controller Layer
        └── ApplicationController.py  # HTTP controllers
```

---

## Setup and Installation

### Step 1: Create Virtual Environment

Create an isolated Python environment to avoid dependency conflicts:

```bash
# Navigate to the server directory
cd d:\EDUCATION\python\APPLICATION\python-rest-client-server\server

# Create virtual environment
python -m venv env
```

### Step 2: Activate Virtual Environment

**On Windows:**
```bash
.\env\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source env/bin/activate
```

After activation, your command prompt should show `(env)` prefix.

### Step 3: Install Required Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install "fastapi[standard]"
pip install uvicorn
pip install pydantic
pip install PyYAML
```

**Verify Installation:**
```bash
pip list
```

---

## Configuration

### Application Configuration Files

#### 1. `resources/application.yml`

YAML configuration file for application and database settings:

```yaml
com:
  adarsh:
    espark:
      application:
        appConfig:
          appName: "Espark Server Application"
        dbConfig:
          dbPath: "db/store/espark.db"          # Path to SQLite database
          dbScript: "db/scripts/espark.sql"     # SQL initialization script
```

**Configuration Properties:**
- `appName`: Application identifier
- `dbPath`: Relative path to SQLite database file
- `dbScript`: SQL script for database initialization

#### 2. `resources/application.properties`

Properties configuration file (for additional settings):

```properties
[general]
key1=value1
key2=value2

[message]
key1=value1
key2=value2
```

### Configuration Loading Process

1. Application reads `application.yml` from `resources/` directory
2. Extracts database configuration
3. Initializes database connection using `dbPath`
4. Runs `dbScript` to create tables if they don't exist
5. Loads properties from `application.properties`

---

## Database Setup

### Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```

**Table: employee**
- `id`: Unique identifier (Auto-incrementing primary key)
- `name`: Employee name (Required, Text)

### SQL Initialization Script

The file `resources/db/scripts/espark.sql` contains the SQL commands to initialize the database.

### Database Operations

The application automatically:
1. Checks if the database file exists
2. Creates the database file if it doesn't exist
3. Executes the SQL script to create tables
4. Maintains the SQLite connection for all operations

---

## Running the Application

### Step 1: Ensure Virtual Environment is Activated

```bash
# Windows
.\env\Scripts\activate.bat

# macOS/Linux
source env/bin/activate
```

### Step 2: Run the Application

```bash
python main.py
```

### Expected Output

```
Starting web application...
Application configuration loaded successfully.
Loading application configuration...
Looking for application.yml at: d:\...\resources\application.yml
Loading database configuration...
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Step 3: Access the Application

**Via Browser:**
- **API Documentation (Swagger UI)**: http://127.0.0.1:8000/docs
- **Alternative Docs (ReDoc)**: http://127.0.0.1:8000/redoc

**Via cURL or API Client (Postman, Insomnia, etc.):**
```bash
curl http://127.0.0.1:8000/v/api/router/employees
```

---

## API Endpoints

The application provides the following REST API endpoints:

### 1. Get All Employees

**Endpoint:** `GET /v/api/router/employees`

**Description:** Retrieve a list of all employees

**Response:**
```json
[
  {
    "employeeId": 1,
    "name": "John Doe"
  },
  {
    "employeeId": 2,
    "name": "Jane Smith"
  }
]
```

**Status Codes:**
- `200 OK`: Successfully retrieved all employees
- `500 Internal Server Error`: Database error

---

### 2. Get Employee by ID

**Endpoint:** `GET /v/api/router/employee/{employeeId}`

**Parameters:**
- `employeeId` (path parameter, integer): The unique identifier of the employee

**Response (Success):**
```json
{
  "employeeId": 1,
  "name": "John Doe"
}
```

**Response (Not Found):**
```json
null
```

**Status Codes:**
- `200 OK`: Employee found
- `404 Not Found`: Employee does not exist
- `500 Internal Server Error`: Database error

---

### 3. Create New Employee

**Endpoint:** `POST /v/api/router/employee`

**Request Body:**
```json
{
  "employeeId": 1,
  "name": "John Doe"
}
```

**Response:**
```json
"John Doe added successfully"
```

**Status Codes:**
- `200 OK`: Employee created successfully
- `400 Bad Request`: Invalid request data
- `500 Internal Server Error`: Database error

---

### 4. Update Employee

**Endpoint:** `PUT /v/api/router/employee/{employeeId}`

**Parameters:**
- `employeeId` (path parameter, integer): The unique identifier of the employee

**Request Body:**
```json
{
  "employeeId": 1,
  "name": "Jane Doe"
}
```

**Response (Success):**
```json
"Jane Doe updated successfully"
```

**Response (Not Found):**
```json
"Employee with ID 999 not found"
```

**Status Codes:**
- `200 OK`: Employee updated successfully
- `404 Not Found`: Employee does not exist
- `400 Bad Request`: Invalid request data
- `500 Internal Server Error`: Database error

---

### 5. Delete Employee

**Endpoint:** `DELETE /v/api/router/employee/{employeeId}`

**Parameters:**
- `employeeId` (path parameter, integer): The unique identifier of the employee

**Response (Success):**
```json
"Employee with ID 1 deleted successfully"
```

**Response (Not Found):**
```json
"Employee with ID 999 not found"
```

**Status Codes:**
- `200 OK`: Employee deleted successfully
- `404 Not Found`: Employee does not exist
- `500 Internal Server Error`: Database error

---

## API Usage Examples

### Example 1: Get All Employees

**Using cURL:**
```bash
curl -X GET "http://127.0.0.1:8000/v/api/router/employees" \
  -H "Content-Type: application/json"
```

**Using Python requests:**
```python
import requests

response = requests.get("http://127.0.0.1:8000/v/api/router/employees")
employees = response.json()
print(employees)
```

**Using JavaScript fetch:**
```javascript
fetch("http://127.0.0.1:8000/v/api/router/employees")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### Example 2: Create a New Employee

**Using cURL:**
```bash
curl -X POST "http://127.0.0.1:8000/v/api/router/employee" \
  -H "Content-Type: application/json" \
  -d "{\"employeeId\": 1, \"name\": \"Alice Johnson\"}"
```

**Using Python requests:**
```python
import requests

employee_data = {
    "employeeId": 1,
    "name": "Alice Johnson"
}

response = requests.post(
    "http://127.0.0.1:8000/v/api/router/employee",
    json=employee_data
)
print(response.json())
```

**Using Postman:**
1. Set method to `POST`
2. URL: `http://127.0.0.1:8000/v/api/router/employee`
3. Headers: `Content-Type: application/json`
4. Body (JSON):
```json
{
  "employeeId": 1,
  "name": "Alice Johnson"
}
```

---

### Example 3: Get Specific Employee

**Using cURL:**
```bash
curl -X GET "http://127.0.0.1:8000/v/api/router/employee/1" \
  -H "Content-Type: application/json"
```

**Using Python requests:**
```python
import requests

employee_id = 1
response = requests.get(f"http://127.0.0.1:8000/v/api/router/employee/{employee_id}")
employee = response.json()
print(employee)
```

---

### Example 4: Update Employee

**Using cURL:**
```bash
curl -X PUT "http://127.0.0.1:8000/v/api/router/employee/1" \
  -H "Content-Type: application/json" \
  -d "{\"employeeId\": 1, \"name\": \"Alice Smith\"}"
```

**Using Python requests:**
```python
import requests

employee_data = {
    "employeeId": 1,
    "name": "Alice Smith"
}

response = requests.put(
    "http://127.0.0.1:8000/v/api/router/employee/1",
    json=employee_data
)
print(response.json())
```

---

### Example 5: Delete Employee

**Using cURL:**
```bash
curl -X DELETE "http://127.0.0.1:8000/v/api/router/employee/1" \
  -H "Content-Type: application/json"
```

**Using Python requests:**
```python
import requests

response = requests.delete("http://127.0.0.1:8000/v/api/router/employee/1")
print(response.json())
```

---

## Code Explanation

### 1. Entry Point: `main.py`

```python
import uvicorn
from fastapi import FastAPI
from src.config.ApplicationConfig import ApplicationConfig
from src.router.ApplicationRouter import ApplicationRouter

def executeWeb():
    print("Starting web application...")
    # Initialize configuration (loads YAML, properties, and sets up database)
    appConfig = ApplicationConfig()
    
    # Create FastAPI application instance
    app = FastAPI()
    
    # Include router with prefix "/v"
    app.router.include_router(
        prefix="/v",
        router=appConfig.getApplicationRouter().getRouter()
    )
    
    # Run the server on localhost:8000
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    executeWeb()
```

**Key Points:**
- Launches Uvicorn server (ASGI server for FastAPI)
- Initializes application configuration
- Sets up API routes with "/v" prefix
- Listens on http://127.0.0.1:8000

---

### 2. Entity: `src/entity/Employee.py`

```python
from pydantic import BaseModel

class Employee(BaseModel):
    employeeId: int
    name: str
    
    def __str__(self):
        return f"Employee ID: {self.employeeId}, Name: {self.name}"
```

**Key Points:**
- Inherits from Pydantic's `BaseModel` for automatic validation
- Defines employee data structure
- `employeeId`: Unique identifier (integer)
- `name`: Employee name (string)
- Pydantic automatically handles JSON serialization/deserialization

---

### 3. Repository: `src/respository/EmployeeRepository.py`

**Purpose:** Database access layer for Employee CRUD operations

**Key Methods:**

```python
def addEmployee(self, employee: Employee) -> str:
    """Insert new employee into database"""
    cursor.execute("INSERT INTO employee (name) VALUES (?)", (employee.name,))
    connection.commit()

def getEmployeeById(self, empId: int) -> Employee:
    """Retrieve employee by ID"""
    cursor.execute("SELECT id, name FROM employee WHERE id = ?", (empId,))
    row = cursor.fetchone()
    if row:
        return Employee(employeeId=row[0], name=row[1])

def getAllEmployees(self) -> list[Employee]:
    """Retrieve all employees"""
    cursor.execute("SELECT id, name FROM employee")
    rows = cursor.fetchall()
    return [Employee(employeeId=row[0], name=row[1]) for row in rows]

def updateEmployee(self, empId: int, employee: Employee) -> str:
    """Update employee information"""
    cursor.execute("UPDATE employee SET name = ? WHERE id = ?", 
                  (employee.name, empId))
    connection.commit()

def deleteEmployee(self, empId: int) -> str:
    """Delete employee from database"""
    cursor.execute("DELETE FROM employee WHERE id = ?", (empId,))
    connection.commit()
```

**Key Features:**
- Uses parameterized queries to prevent SQL injection
- Exception handling for database errors
- Returns typed objects (Employee or list[Employee])
- Commits transactions after modifications

---

### 4. Service: `src/services/EmployeeService.py`

**Purpose:** Business logic layer for employee operations

```python
class EmployeeService:
    def __init__(self, employeeRepository: EmployeeRepository):
        self.employeeRepository = employeeRepository
    
    def getEmployeeById(self, employeeId: int) -> Employee:
        """Get single employee - delegates to repository"""
        return self.employeeRepository.getEmployeeById(employeeId)
    
    def getAllEmployees(self) -> list[Employee]:
        """Get all employees"""
        return self.employeeRepository.getAllEmployees()
    
    def addEmployee(self, employee: Employee) -> str:
        """Add new employee with validation"""
        self.employeeRepository.addEmployee(employee)
        return f"{employee.name} added successfully"
    
    def updateEmployee(self, employeeId: int, employee: Employee) -> str:
        """Update employee with existence check"""
        if self.employeeRepository.getEmployeeById(employeeId):
            self.employeeRepository.updateEmployee(employeeId, employee)
            return f"{employee.name} updated successfully"
        else:
            return f"Employee with ID {employeeId} not found"
    
    def deleteEmployee(self, employeeId: int) -> str:
        """Delete employee with existence check"""
        if self.employeeRepository.getEmployeeById(employeeId):
            self.employeeRepository.deleteEmployee(employeeId)
            return f"Employee with ID {employeeId} deleted successfully"
        else:
            return f"Employee with ID {employeeId} not found"
```

**Key Points:**
- Validates employee existence before update/delete
- Provides meaningful response messages
- Orchestrates repository operations
- Separates business logic from data access

---

### 5. Router: `src/router/ApplicationRouter.py`

**Purpose:** Defines and manages API routes

```python
from fastapi import APIRouter
from src.entity.Employee import Employee

class ApplicationRouter:
    def __init__(self, employeeService: EmployeeService):
        self.router = APIRouter()
        self.service = employeeService
        
        # Register routes
        self.router.add_api_route(
            "/api/router/employee/{employeeId}",
            self.get_employee,
            methods=["GET"]
        )
        self.router.add_api_route(
            "/api/router/employees",
            self.get_all_employees,
            methods=["GET"]
        )
        # ... other routes
    
    def getRouter(self) -> APIRouter:
        return self.router
    
    def get_employee(self, employeeId: int) -> Employee:
        return self.service.getEmployeeById(employeeId)
    
    # ... other endpoint methods
```

**Key Points:**
- Creates FastAPI APIRouter instance
- Registers HTTP endpoints
- Maps HTTP methods to service methods
- Returns router for inclusion in main app

---

### 6. Configuration: `src/config/ApplicationConfig.py`

**Purpose:** Application initialization and dependency injection

```python
class ApplicationConfig:
    def __init__(self):
        # Load YAML configuration
        self.ymlReader = YamlReader(ymlFilePath)
        self.dbConfig = self.ymlReader.getDbConfig()
        
        # Load properties configuration
        self.propertiesReader = PropertiesReader(propertiesFilePath)
        
        # Initialize database
        self.loadDbConfig()
    
    def loadDbConfig(self) -> None:
        """Initialize database connection and run SQL script"""
        dbConnection = DbConnection(dbPath)
        InitializedDb(dbConnection, sqlScriptPath)
    
    def getApplicationRouter(self) -> ApplicationRouter:
        """Create and return configured router"""
        employeeRepository = EmployeeRepository(dbConnection)
        employeeService = EmployeeService(employeeRepository)
        return ApplicationRouter(employeeService)
```

**Key Points:**
- Centralizes configuration loading
- Implements dependency injection pattern
- Initializes database on startup
- Manages component lifecycle

---

### 7. Database Connection: `src/config/persistance/DbConection.py`

**Purpose:** Thread-safe database connection management

```python
class DbConnection:
    def __init__(self, dbName: str):
        self.dbName = dbName
        self.local = threading.local()  # Thread-local storage
    
    def getDBConnection(self) -> sqlite3.Connection:
        """Get or create database connection for current thread"""
        if not hasattr(self.local, 'connection'):
            self.local.connection = sqlite3.connect(self.dbName)
        return self.local.connection
    
    def getDBCursor(self) -> sqlite3.Cursor:
        """Get or create database cursor for current thread"""
        if not hasattr(self.local, 'cursor'):
            self.local.cursor = self.getDBConnection().cursor()
        return self.local.cursor
```

**Key Points:**
- Uses thread-local storage for thread safety
- Lazy initialization of connections
- Prevents connection conflicts in multi-threaded environment
- Creates connection only when needed

---

## Complete Workflow

```
1. User sends HTTP request to /v/api/router/employee/1
                ↓
2. FastAPI routes request to ApplicationRouter.get_employee(1)
                ↓
3. Router delegates to EmployeeService.getEmployeeById(1)
                ↓
4. Service calls EmployeeRepository.getEmployeeById(1)
                ↓
5. Repository queries SQLite database
                ↓
6. Repository returns Employee object
                ↓
7. Service returns Employee object
                ↓
8. Router returns Employee as JSON response
                ↓
9. FastAPI serializes to JSON and sends to client
```

---

## Troubleshooting

### Issue 1: "application.yml file not found"

**Error Message:**
```
Error: application.yml file not found in resources directory.
```

**Solution:**
- Verify `resources/application.yml` exists
- Check file path and permissions
- Ensure you're running from the correct directory

---

### Issue 2: "Database connection error"

**Error Message:**
```
Error: sqlite3.OperationalError: [database name] cannot open
```

**Solution:**
- Check if `resources/db/store/` directory exists
- Create directory if missing: `mkdir resources\db\store`
- Verify write permissions
- Check `dbPath` in `application.yml`

---

### Issue 3: "ModuleNotFoundError" for FastAPI

**Error Message:**
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution:**
- Ensure virtual environment is activated
- Install dependencies: `pip install "fastapi[standard]"`
- Verify installation: `pip list`

---

### Issue 4: "Port 8000 already in use"

**Error Message:**
```
OSError: [Errno 10048] Only one usage of each socket address
```

**Solution:**
- Kill process using port 8000:
  - **Windows:** `netstat -ano | findstr :8000` then `taskkill /PID [PID] /F`
  - **macOS/Linux:** `lsof -i :8000` then `kill -9 [PID]`
- Or change port in `main.py`: `uvicorn.run(app, port=8001)`

---

### Issue 5: "Employee not found" when retrieving

**Cause:** Employee doesn't exist or wrong ID used

**Solution:**
- Use GET `/v/api/router/employees` to see all employees
- Verify the employee ID is correct
- Create employees before retrieving them

---

## Performance Tips

1. **Connection Pooling:** For production, use connection pooling library
2. **Indexing:** Add database indexes on frequently queried columns
3. **Caching:** Implement caching for frequently accessed data
4. **Pagination:** Add limit/offset for large result sets
5. **Logging:** Implement proper logging for debugging

---

## Security Considerations

1. **Input Validation:** Implemented via Pydantic models
2. **SQL Injection Prevention:** Uses parameterized queries
3. **CORS:** Add CORS middleware for cross-origin requests
4. **Authentication:** Add JWT or OAuth for production
5. **Rate Limiting:** Implement rate limiting to prevent abuse

---

## Next Steps / Enhancements

1. Add employee email and phone fields
2. Implement employee department/role
3. Add pagination and filtering
4. Implement authentication and authorization
5. Add logging and monitoring
6. Write unit tests
7. Add API request validation
8. Implement soft deletes
9. Add database migrations
10. Deploy to production server

---

## Contact & Support

For questions or issues, refer to the code comments or check the Swagger UI documentation at:
http://127.0.0.1:8000/docs

---

**Last Updated:** February 17, 2026
**Version:** 1.0.0