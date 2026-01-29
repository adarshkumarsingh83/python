# Fibonacci Generator

This project contains a simple Fibonacci number generator implemented in Python.

## Overview
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. This generator will yield Fibonacci numbers indefinitely.

## Code Explanation

### `generate_numbers()` Function
- **Type**: `Generator[int, None, None]`
- **Description**: This function generates Fibonacci numbers indefinitely. It uses a `while True` loop to yield the next number in the sequence each time it is called.

### `main()` Function
- **Type**: `None`
- **Description**: This function serves as the entry point of the program. It prompts the user to press Enter to receive the next `n` Fibonacci numbers, where `n` is set to 10 by default.

## How to Run the Code
1. Ensure you have Python installed on your machine.
2. Clone this repository or download the `main.py` file.
3. Open a terminal and navigate to the directory containing `main.py`.
4. Run the script using the command:
   ```bash
   python main.py
   ```
5. Follow the prompts in the terminal to generate Fibonacci numbers.

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
