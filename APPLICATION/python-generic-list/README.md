# Python Generic List Processor

A Python application demonstrating the use of generics (introduced in Python 3.12) to create a type-safe, reusable data processor that can handle lists of any data type.

## Overview

This project showcases Python's generic type system through a `DataProcessor` class that can process collections of different types (strings, integers, custom objects) while maintaining type safety at runtime. The application demonstrates how generics enable code reusability and type checking for polymorphic operations.

## Features

- **Generic Data Processing**: A single `DataProcessor` class that works with any data type
- **Type Safety**: Leverages Python's type hints and generics for compile-time type checking
- **Custom Object Support**: Demonstrates processing of custom classes like `Employee`
- **Multiple Data Types**: Shows processing of strings, integers, and custom objects
- **Simple Architecture**: Clean separation of concerns with dedicated packages for beans and processors

## Project Structure

```
python-generic-list/
├── main.py                 # Main application entry point with demonstration
├── README.md              # Project documentation
├── bean/                  # Data model classes
│   └── Employee.py        # Employee class definition
└── processor/             # Business logic classes
    └── DataProcessor.py   # Generic data processor implementation
```

## Requirements

- Python 3.12 or higher (for generic type support)
- No external dependencies required

## Installation

1. Clone or download the project files
2. Ensure Python 3.12+ is installed on your system
3. Navigate to the project directory

## Usage

### Running the Application

Execute the main script to see the generic processor in action:

```bash
python main.py
```

### Example Output

The application demonstrates processing three different types of lists:

1. **String List Processing**:
   ```
   Processed item: Hello
   Processed item: World
   Processed item: Python
   Processed item: Generics
   response Generics
   response Python
   response World
   response Hello
   ```

2. **Integer List Processing**:
   ```
   Processed item: 1
   Processed item: 2
   Processed item: 3
   Processed item: 4
   Processed item: 5
   response 5
   response 4
   response 3
   response 2
   response 1
   ```

3. **Employee Object Processing**:
   ```
   Processed item: Employee(id=E001, name='Alice')
   Processed item: Employee(id=E002, name='Bob')
   Processed item: Employee(id=E003, name='Charlie')
   Processed item: Employee(id=E004, name='Diana')
   Employee(id=E004, name='Diana')
   Employee(id=E003, name='Charlie')
   Employee(id=E002, name='Bob')
   Employee(id=E001, name='Alice')
   ```

## Code Explanation

### DataProcessor Class

The core of the application is the generic `DataProcessor[T]` class:

```python
class DataProcessor[T]:
    def processData(self, dataItem: list[T]) -> list[T]:
        # Process each item
        for item in dataItem:
            print(f"Processed item: {item}")
        # Return reversed list as demonstration
        return dataItem[::-1]
```

### Employee Class

A simple data model class:

```python
class Employee:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Employee(id={self.id}, name='{self.name}')"
```

### Main Execution

The `main.py` file instantiates the generic processor for different types:

```python
# String processing
dataProcessor: DataProcessor[str] = DataProcessor[str]()
responseItems = dataProcessor.processData(stringList)

# Integer processing
dataProcessor: DataProcessor[int] = DataProcessor[int]()
responseItems = dataProcessor.processData(integerList)

# Custom object processing
dataProcessor: DataProcessor[Employee] = DataProcessor[Employee]()
responseItems = dataProcessor.processData(employeeList)
```

## Key Concepts Demonstrated

- **Generics in Python**: Using `[T]` type parameters for generic classes
- **Type Hints**: Proper type annotations for parameters and return values
- **Polymorphism**: Single implementation working with multiple types
- **Custom Classes**: Integration with user-defined classes
- **List Operations**: Processing collections of various types

## Extending the Project

To extend this project, you could:

- Add more complex processing logic in `DataProcessor.processData()`
- Create additional data model classes
- Implement different processing strategies (sorting, filtering, transformation)
- Add error handling and validation
- Create unit tests for the generic functionality

## Learning Outcomes

This project helps understand:

- How Python's type system supports generics
- The benefits of type-safe generic programming
- Code reusability through parametric polymorphism
- Integration of generics with custom classes
- Practical application of type hints in Python