# Python FastAPI REST Application

A simple REST API built with FastAPI for managing employee records. This application demonstrates a basic CRUD (Create, Read, Update, Delete) API with in-memory data storage.

## Features

- **GET** `/v/api/router/employee/{employeeId}` - Retrieve a specific employee by ID
- **GET** `/v/api/router/employees` - Retrieve all employees
- **POST** `/v/api/router/employee` - Add a new employee
- **PUT** `/v/api/router/employee/{employeeId}` - Update an existing employee
- **DELETE** `/v/api/router/employee/{employeeId}` - Delete an employee by ID

## Project Structure

```
python-fastapi-rest/
├── main.py                    # Application entry point
├── README.md                  # Project documentation
├── bean/
│   └── Employee.py           # Employee data model (Pydantic)
├── router/
│   └── ApplicationRouter.py  # API route definitions
├── service/
│   └── EmployeeService.py    # Business logic and data management
├── web/
│   └── ApplicationController.py  # Alternative controller implementation (not used)
└── env/                      # Virtual environment (created during setup)
```

## Architecture Overview

### Data Layer (`bean/Employee.py`)
- Defines the `Employee` model using Pydantic BaseModel
- Contains `employeeId` (int) and `name` (str) fields
- Provides string representation for debugging

### Service Layer (`service/EmployeeService.py`)
- Manages employee data operations
- Uses in-memory dictionary for data storage (not persistent)
- Implements CRUD operations:
  - `getEmployeeById(employeeId)` - Retrieves employee by ID
  - `getAllEmployees()` - Returns all employees
  - `addEmployee(employee)` - Adds new employee
  - `updateEmployee(employeeId, employee)` - Updates existing employee
  - `deleteEmployee(employeeId)` - Removes employee by ID

### Router Layer (`router/ApplicationRouter.py`)
- Defines API endpoints using FastAPI's APIRouter
- Routes are prefixed with `/v` in the main application
- Maps HTTP methods to service methods
- Handles request/response serialization automatically via Pydantic

### Entry Point (`main.py`)
- Creates FastAPI application instance
- Includes the ApplicationRouter with `/v` prefix
- Starts uvicorn server on `127.0.0.1:8000`

### Alternative Implementation (`web/ApplicationController.py`)
- Contains an alternative implementation using FastAPI decorators directly
- Not currently used in the application
- Provides the same functionality as ApplicationRouter but with different routing approach

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv env
```

### 2. Activate Virtual Environment
**Windows:**
```bash
.\env\Scripts\activate.bat
```
**Linux/Mac:**
```bash
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install "fastapi[standard]"
```

## Running the Application

1. Ensure virtual environment is activated
2. Run the application:
```bash
python main.py
```
3. The server will start on `http://127.0.0.1:8000`

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Sample API Usage

### Get All Employees
```bash
GET http://127.0.0.1:8000/v/api/router/employees
```

### Get Employee by ID
```bash
GET http://127.0.0.1:8000/v/api/router/employee/1
```

### Add New Employee
```bash
POST http://127.0.0.1:8000/v/api/router/employee
Content-Type: application/json

{
  "employeeId": 4,
  "name": "John Doe"
}
```

### Update Employee
```bash
PUT http://127.0.0.1:8000/v/api/router/employee/4
Content-Type: application/json

{
  "employeeId": 4,
  "name": "Jane Doe"
}
```

### Delete Employee
```bash
DELETE http://127.0.0.1:8000/v/api/router/employee/4
```

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation and serialization

## Notes

- Data is stored in memory only and will be lost when the application restarts
- No authentication or authorization implemented
- Basic error handling is present but could be enhanced
- The `ApplicationController.py` file contains an alternative implementation that's not currently used

