# Python FastAPI SQLite CRUD Application

A robust REST API built with FastAPI and SQLite for managing employee records. This application demonstrates a clean architecture with separation of concerns, including configuration management, dependency injection, and proper error handling.

## Features

- **RESTful API**: Complete CRUD operations for employee management
- **SQLite Database**: Lightweight, file-based database with automatic schema initialization
- **FastAPI Framework**: High-performance, modern Python web framework
- **Pydantic Models**: Data validation and serialization
- **Thread-Safe Database**: Proper handling of SQLite connections in multi-threaded environment
- **YAML Configuration**: Externalized configuration using YAML files
- **Auto-generated Documentation**: Interactive API documentation via Swagger UI

## Project Structure

```
python-fastapi-sqllight-crud/
├── main.py                          # Application entry point
├── README.md                        # Project documentation
├── env/                             # Virtual environment
├── resources/                       # Configuration and database files
│   ├── application.properties       # Application properties
│   ├── application.yml             # YAML configuration
│   └── db/
│       ├── scripts/
│       │   └── espark.sql          # Database schema and initial data
│       └── store/
│           └── espark.db            # SQLite database file (auto-generated)
└── src/                             # Source code
    ├── config/                      # Configuration management
    │   ├── ApplicationConfig.py     # Main application configuration
    │   ├── PropertiesReader.py      # Properties file reader
    │   ├── YamlReader.py           # YAML file reader
    │   ├── bean/                   # Configuration beans
    │   └── persistance/            # Database configuration
    │       ├── DbConection.py      # Thread-safe database connection
    │       └── InitializedDb.py    # Database initialization
    ├── entity/                     # Data models
    │   └── Employee.py             # Employee Pydantic model
    ├── respository/                # Data access layer
    │   └── EmployeeRepository.py   # Employee database operations
    ├── router/                     # API routing
    │   └── ApplicationRouter.py    # FastAPI route definitions
    ├── services/                   # Business logic layer
    │   └── EmployeeService.py      # Employee business operations
    └── web/                        # Web layer (alternative controllers)
        └── ApplicationController.py # Alternative FastAPI controllers
```

## Prerequisites

- **Python 3.8+**: Make sure Python is installed on your system
- **Git**: For cloning the repository (optional)

## Installation

### 1. Clone the Repository (Optional)

```bash
git clone <repository-url>
cd python-fastapi-sqllight-crud
```

### 2. Create Virtual Environment

Create a virtual environment to isolate project dependencies:

**Windows:**
```bash
python -m venv env
```

**Linux/Mac:**
```bash
python3 -m venv env
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.\env\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source env/bin/activate
```

### 4. Install Dependencies

Install FastAPI and all required dependencies:

```bash
pip install "fastapi[standard]"
```

This command installs:
- **fastapi**: The main web framework
- **uvicorn**: ASGI server for running the application
- **pydantic**: Data validation and serialization
- **starlette**: ASGI toolkit
- Additional standard dependencies

### 5. Verify Installation

Check that all packages are installed correctly:

```bash
pip list
```

You should see packages like:
- fastapi (0.129.0)
- uvicorn (0.40.0)
- pydantic (2.12.5)
- starlette (0.52.1)
- And other dependencies

## Configuration

The application uses external configuration files:

### application.yml
Located at `resources/application.yml`, contains:
- Application name
- Database path and script location

### application.properties
Located at `resources/application.properties`, contains additional properties.

### Database Configuration
- **Database File**: `resources/db/store/espark.db` (auto-created)
- **Schema Script**: `resources/db/scripts/espark.sql`
- **Initial Data**: Pre-populated with sample employee records

## Running the Application

### Development Mode

Run the web application:

```bash
python main.py
```

This starts the FastAPI server on `http://127.0.0.1:8000`

### Alternative: Direct Uvicorn

You can also run the server directly with uvicorn:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Testing Mode

The application includes a test mode that demonstrates CRUD operations:

Modify `main.py` to run `executeMain()` instead of `executeWeb()` for console-based testing.

## API Endpoints

Once running, the API provides the following endpoints:

### Base URL
```
http://127.0.0.1:8000/v
```

### Employee Management

#### Get All Employees
- **GET** `/api/router/employees`
- **Response**: List of all employees
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

#### Get Employee by ID
- **GET** `/api/router/employee/{employeeId}`
- **Response**: Single employee object or null if not found

#### Add New Employee
- **POST** `/api/router/employee`
- **Body**:
```json
{
  "employeeId": 0,
  "name": "New Employee"
}
```

#### Update Employee
- **PUT** `/api/router/employee/{employeeId}`
- **Body**: Employee object with updated data

#### Delete Employee
- **DELETE** `/api/router/employee/{employeeId}`
- **Response**: Success message

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Database Schema

The SQLite database contains one main table:

```sql
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```

**Initial Data**: The database is pre-populated with sample employees:
- adarsh
- radha
- sonu
- monu
- shakti

## Architecture Overview

### Layered Architecture
1. **Web Layer**: FastAPI routes and controllers
2. **Service Layer**: Business logic and validation
3. **Repository Layer**: Data access and database operations
4. **Configuration Layer**: External configuration management

### Key Components

- **ApplicationConfig**: Central configuration management
- **DbConnection**: Thread-safe SQLite connection management
- **EmployeeRepository**: Database CRUD operations
- **EmployeeService**: Business logic for employee management
- **ApplicationRouter**: FastAPI route definitions

### Thread Safety
The application properly handles SQLite's threading limitations by using thread-local storage for database connections, ensuring safe concurrent access in production environments.

## Development

### Code Style
- Follow PEP 8 Python style guidelines
- Use type hints for better code documentation
- Maintain separation of concerns across layers

### Adding New Features
1. Define data models in `src/entity/`
2. Implement repository methods in `src/repository/`
3. Add business logic in `src/services/`
4. Create API routes in `src/router/`
5. Update configuration as needed

### Testing
- Use FastAPI's built-in testing tools
- Test database operations with SQLite in-memory database
- Validate API responses with Pydantic models

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   - Change the port in `main.py` or kill the process using port 8000

2. **Database Connection Errors**
   - Ensure the `resources/db/store/` directory exists
   - Check file permissions for database file

3. **Import Errors**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed

4. **Threading Errors**
   - The application handles SQLite threading automatically
   - If issues persist, check concurrent request handling

### Logs
Application logs are printed to the console. Check for error messages during startup and API calls.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues:
- Check the API documentation at `/docs`
- Review the code comments
- Create an issue in the repository

---

**Happy Coding! 🚀**