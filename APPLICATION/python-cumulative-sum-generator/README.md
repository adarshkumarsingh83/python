# Cumulative Sum Generator

A Python application that demonstrates the use of generator functions with the `yield` statement to maintain and calculate cumulative sums interactively.

## Overview

This application implements a **generator-based cumulative sum calculator** that allows users to continuously add numbers and receive a running total. It showcases advanced Python concepts like generators, two-way communication between caller and generator using `yield`, and type hints.

## Features

- **Generator-based architecture**: Uses Python generators to maintain state across multiple iterations
- **Interactive input**: Accepts user input to add numbers to the cumulative sum
- **Error handling**: Validates numeric input and handles invalid entries gracefully
- **Type hints**: Includes full type annotations for better code clarity and IDE support

## How It Works

The program uses a generator function `generate_numbers()` that:
1. Maintains a running total using internal state
2. Yields the current total to the caller
3. Receives new increments via the `send()` method
4. Updates the total with each increment

The main loop:
1. Prompts the user to enter a number or type 'exit' to quit
2. Sends the number to the generator
3. Receives and displays the updated cumulative sum
4. Handles invalid input with error messages

## Requirements

- Python 3.7 or higher

## Installation

No external dependencies are required. This application uses only Python's standard library.

## How to Execute

### Method 1: Direct Execution
```bash
python main.py
```

### Method 2: Using Python Command
```bash
python d:\EDUCATION\python\APPLICATION\python-cumulative-sum-generator\main.py
```

### Method 3: Interactive Mode (Windows PowerShell)
```powershell
cd d:\EDUCATION\python\APPLICATION\python-cumulative-sum-generator
python main.py
```

## Usage Example

```
Enter a number to add (or 'exit' to quit): 10
Current total: 10.0
Enter a number to add (or 'exit' to quit): 5
Current total: 15.0
Enter a number to add (or 'exit' to quit): 8.5
Current total: 23.5
Enter a number to add (or 'exit' to quit): exit
```

## Code Structure

### Main Components

**`generate_numbers()` - Generator Function**
- Returns a generator that yields float values
- Maintains a `total` variable that accumulates increments
- Accepts numbers via the `send()` method
- Yields the current total after each increment

**`main()` - Main Function**
- Initializes the generator and primes it with `next()`
- Enters an infinite loop to accept user input
- Sends user input to the generator using `send()`
- Displays the current cumulative sum
- Handles `ValueError` for invalid numeric input
- Exits on 'exit' command

## Key Python Concepts Demonstrated

1. **Generators**: Functions that use `yield` to produce values lazily
2. **Two-way communication**: Using `yield` to receive values via `send()`
3. **Type hints**: Full type annotations including `Generator[YieldType, SendType, ReturnType]`
4. **Exception handling**: Try-except blocks for input validation
5. **String methods**: Using `.lower()` for case-insensitive comparison

## Notes

- Numbers can be positive or negative
- The program accepts decimal numbers (e.g., 8.5)
- Invalid input (non-numeric) triggers an error message and re-prompts
- Type 'exit' or 'EXIT' to terminate the program
