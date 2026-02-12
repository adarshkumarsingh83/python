# Python Generics Object Tutorial

## Project Overview

This is an educational project demonstrating **Python Generic Types** (introduced in Python 3.12+) using type hints. The application showcases how to create generic classes that work with different data types while maintaining type safety.

## Purpose

This project demonstrates:
- Generic class implementation using square bracket notation `Class[T]`
- Type-safe message handling across multiple message types
- Practical use of type hints in Python
- Object-oriented design with reusable components

## Project Structure

```
python-generics-object/
├── main.py                          # Entry point with example usage
├── README.md                        # Project documentation
├── beans/                           # Message domain objects
│   ├── GreetMessage.py             # Greeting message class
│   ├── WishMessage.py              # Wish message class
│   └── __pycache__/
└── services/                        # Business logic services
    ├── MessageService.py           # Generic message service
    └── __pycache__/
```

## Components

### 1. beans/GreetMessage.py
`GreetMessage` class represents a greeting message.

**Attributes:**
- `id` (str): Unique identifier for the message
- `senderId` (str): ID of the sender
- `content` (str): The greeting content

**Methods:**
- `getGreeting()`: Returns the greeting content
- `__str__()`: String representation of the message

### 2. beans/WishMessage.py
`WishMessage` class represents a wish message.

**Attributes:**
- `id` (str): Unique identifier for the message
- `senderId` (str): ID of the sender
- `content` (str): The wish content

**Methods:**
- `getWish()`: Returns the wish content
- `__str__()`: String representation of the message

### 3. services/MessageService.py
`MessageService[T]` is a **generic service** that handles any message type.

**Features:**
- Uses generic type parameter `T` to accept any message type
- Provides type safety without code duplication
- Works with both `GreetMessage` and `WishMessage`

**Methods:**
- `__init__(message: T)`: Initialization with a message of type T
- `getMessage()`: Returns the formatted message

## Requirements

- Python 3.12+ (for PEP 695 generic syntax) or Python 3.9+ (with `from __future__ import annotations`)
- No external dependencies

## Usage

Run the application:

```bash
python main.py
```

### Example Code

```python
from beans.GreetMessage import GreetMessage
from services.MessageService import MessageService

# Create a greeting message
greetMessage = GreetMessage("1", "sender1", "Hello, how are you?")

# Create a service for this message type
greetService = MessageService(greetMessage)

# Retrieve and display the message
print(greetService.getMessage())
```

## Output Example

```
Message: GreetMessage(id=1, senderId=sender1, content=Hello, how are you?)
Message: GreetMessage(id=2, senderId=sender2, content=Happy Birthday!)
```

## Key Concepts Demonstrated

### Generic Types
The `MessageService[T]` class is generic, meaning it can work with any type `T`:

```python
from __future__ import annotations

class MessageService[T]:
    def __init__(self, message: T):
        self.message = message
    
    def getMessage(self) -> T:
        return f"Message: {self.message.__str__()}"
```

This allows creating multiple service instances for different message types:
- `MessageService[GreetMessage]` - for greetings
- `MessageService[WishMessage]` - for wishes

### Type Safety
With generics, you get:
- IDE autocomplete support
- Static type checking with tools like mypy
- Better code documentation
- Reduced runtime errors

## Learning Path

1. Start with [beans/GreetMessage.py](beans/GreetMessage.py) - Simple class definition
2. Read [beans/WishMessage.py](beans/WishMessage.py) - Similar structure
3. Study [services/MessageService.py](services/MessageService.py) - Generic implementation
4. Run [main.py](main.py) - See it in action

## Extensions

You can extend this project by:
- Adding more message types (AlertMessage, ErrorMessage, etc.)
- Implementing message filtering in MessageService
- Adding a message repository pattern
- Creating a message queue system
- Adding async/await support

## Notes

- Python 3.12+ supports generic syntax directly (`class MessageService[T]:`)
- Earlier versions require `from __future__ import annotations` and `Generic` from typing module
- This is a tutorial project for learning purposes
