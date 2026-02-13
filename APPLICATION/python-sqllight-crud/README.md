# Python SQLite CRUD Application

A simple Python application demonstrating CRUD (Create, Read, Update, Delete) operations on an Employee entity using SQLite database.

## Features

- **Employee Management**: Full CRUD operations for employee records
- **Configuration Management**: YAML and Properties file-based configuration
- **Database Initialization**: Automatic database setup with SQL scripts
- **Layered Architecture**: Clean separation of concerns with config, persistence, and repository layers

## Project Structure

```
python-sqllight-crud/
├── main.py                          # Application entry point
├── README.md                        # Project documentation
├── resources/
│   ├── application.properties       # Properties configuration file
│   ├── application.yml              # YAML configuration file
│   └── db/
│       ├── script/
│       │   └── espark.sql           # Database initialization script
│       └── store/
│           └── espark.db             # SQLite database file (created at runtime)
└── src/
    ├── config/
    │   ├── ApplicationConfig.py     # Main configuration loader
    │   ├── PropertiesReader.py      # Properties file reader
    │   ├── YamlReader.py            # YAML file reader
    │   ├── bean/
    │   │   └── ConfigurationBean.py # Configuration data classes
    │   └── persistance/
    │       ├── DbConection.py       # Database connection manager
    │       └── initializedDb.py     # Database initialization
    └── respository/
        └── EmployeeRepository.py    # Employee data access layer
```

## Installation

1. **Clone or download** the project to your local machine.

2. **Navigate** to the project directory:
   ```bash
   cd python-sqllight-crud
   ```

3. **Ensure Python 3.6+** is installed on your system.

4. **No external dependencies** are required as the application uses only built-in Python modules (sqlite3, os, yaml, etc.).

## Configuration

The application uses two configuration files located in the `resources/` directory:

### application.yml
Contains application and database configuration:
```yaml
com:
  adarsh:
    espark:
      application:
        appConfig:
          appName: "Espark sqllight Application"
        dbConfig:
          dbPath: "db/store/espark.db"
          dbScript: "db/script/espark.sql"
```

### application.properties
Contains additional properties (currently sample data):
```properties
[general]
key1=value1
key2=value2

[message]
key1=value1
key2=value2
```

## Usage

Run the application using Python:

```bash
python main.py
```

The application will:
1. Load configuration from YAML and properties files
2. Initialize the SQLite database using the SQL script
3. Perform CRUD operations on employee records:
   - Display all employees
   - Add a new employee
   - Update an existing employee
   - Delete an employee
   - Display final employee list

## Database Schema

The application creates an `employee` table with the following structure:

```sql
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```

Initial data includes sample employees: adarsh, radha, sonu, monu, shakti.

## Architecture Overview

### Layers:
- **Config Layer** (`src/config/`): Handles configuration loading and parsing
- **Persistence Layer** (`src/config/persistance/`): Manages database connections
- **Repository Layer** (`src/respository/`): Provides data access methods

### Key Classes:
- `ApplicationConfig`: Central configuration manager
- `EmployeeRepository`: Employee CRUD operations
- `DbConnection`: SQLite database connection wrapper
- `YamlReader` & `PropertiesReader`: Configuration file parsers

## Dependencies

- Python 3.6+
- Built-in modules: `sqlite3`, `os`, `dataclasses`, `typing`, `yaml`

## Error Handling

The application includes basic error handling for:
- File not found errors (configuration files)
- Database connection issues
- SQL execution errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check for any applicable licenses.

## Author

Developed as a demonstration of Python SQLite CRUD operations.