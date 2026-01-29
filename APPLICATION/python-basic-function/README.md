# Python Basic Function

## Description

This Python program demonstrates a basic function implementation that greets a user by name.

## What It Does

The program performs a simple greeting operation:
1. Prompts the user to enter their name via console input
2. Passes the entered name to a `greet()` function
3. Displays a personalized greeting message to the user

## How It Works

### Function: `greet(name: str) -> str`

- **Purpose**: Creates and returns a personalized greeting message
- **Parameter**: `name` (string) - The person's name to greet
- **Return Type**: String - The formatted greeting message
- **Logic**: Uses an f-string to combine the text "Hello, " with the provided name and an exclamation mark

### Main Execution Block: `if __name__ == "__main__":`

- **Purpose**: Ensures the code runs only when the script is executed directly (not when imported)
- **Process**:
  1. `input("Enter your name: ")` - Displays a prompt and waits for user input
  2. `greet(user_name)` - Calls the function with the entered name
  3. `print()` - Outputs the returned greeting message to the console

## Example Usage

```
Enter your name: Alice
Hello, Alice!
```

## Technical Details

- **Type Hints**: The function uses type annotations (`name: str` and `-> str`) to indicate parameter and return types
- **F-string Formatting**: Modern Python string formatting technique for embedding variables in strings
- **Main Guard Pattern**: The `if __name__ == "__main__"` pattern is a Python best practice for script entry points
