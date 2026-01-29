# File Reading Project

## Overview
This is a Python project demonstrating file reading and data processing capabilities using generators and interactive user input. The project reads a narrative-based data file containing a complete 100-line story line by line.

## Project Structure
- **data.txt** - Contains a complete 100-line story titled "The Lost City of Meridia" - an archaeological adventure narrative
- **main.py** - Python script for reading and processing the story data from data.txt interactively
- **README.md** - This documentation file

## Story Description
The data.txt file contains "The Lost City of Meridia," a 10-chapter story about an archaeological discovery:

### Plot Summary
Dr. Sarah Chen leads a team of archaeologists on an expedition to discover the legendary lost city of Meridia, based on clues from an ancient manuscript. The story unfolds across 10 chapters:

1. **The Beginning** - Introduction to Dr. Chen's quest and her team assembly
2. **The Journey** - The expedition through the desert searching for Meridia
3. **The Discovery** - The revelation of the ancient city emerging from the sand
4. **Secrets Revealed** - Finding a grand library with thousands of preserved stone tablets
5. **The Great Temple** - Exploring the city's most magnificent structure with advanced astronomical knowledge
6. **The Hidden Archive** - Uncovering philosophical and scientific treatises ahead of their time
7. **Personal Artifacts** - Discovering everyday items that reveal the rich culture of the Meridians
8. **The Final Questions** - Reflecting on the implications of the discovery
9. **The Broader Impact** - The worldwide significance and legacy of finding Meridia
10. **Epilogue** - Ten years later, the establishment of a museum and lasting impact

### Key Themes
- Archaeological discovery and exploration
- Lost civilizations and forgotten knowledge
- Teamwork and perseverance in pursuing historical truth
- The preservation and significance of human achievement
- Advanced knowledge in ancient times

## Python Code Description

### main.py Overview
The main.py file implements an interactive file reading system that allows users to read the story line by line at their own pace using generators for memory efficiency.

### Key Components

#### 1. Imports
```python
import sys 
from typing import Generator
```
- **sys** - Used for system operations, specifically `sys.exit()` to terminate the program gracefully
- **typing.Generator** - Type hint for the generator function that yields file lines

#### 2. readFile() Function
```python
def readFile(path: str) -> Generator[str, None, str]:
    """Reads a file line by line."""
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()
```

**Purpose**: Creates a generator that reads a file line by line without loading the entire file into memory

**Parameters**:
- `path` (str) - The file path to read (e.g., 'data.txt')

**Return Type**: `Generator[str, None, str]`
- Yields individual lines as strings
- Each line is stripped of whitespace using `.strip()`

**How It Works**:
1. Opens the file in read mode using a context manager (`with` statement)
2. Iterates through each line in the file
3. Yields each line after removing leading/trailing whitespace
4. Automatically closes the file when the generator is exhausted

**Benefits**:
- Memory efficient - doesn't load entire file into memory
- Lazy evaluation - only reads lines when requested
- Clean resource management with context manager

#### 3. main() Function
```python
def main() -> None:
    reader : Generator[str, None, str] = readFile('data.txt')
    input('Press Enter to start reading the file...')
    while True:
        try:
            line = next(reader)
            print(line)
        except StopIteration as e:
            print('End of file reached.',e.value)
            sys.exit(0)
        input('Press Enter to read the next line...')
```

**Purpose**: Main program loop that handles interactive file reading with user input

**How It Works**:
1. Calls `readFile('data.txt')` to create a generator
2. Waits for user input before starting to read
3. Uses an infinite loop to read one line at a time:
   - Calls `next(reader)` to get the next line from the generator
   - Prints the line to the console
   - Waits for user input to continue to the next line
4. Catches `StopIteration` exception when all lines are read
5. Prints a completion message and exits the program

**User Interaction**:
- Press Enter to start reading
- Press Enter after each line to read the next line
- The program terminates automatically when the file ends

#### 4. Entry Point
```python
if __name__ == '__main__':
    main()
```
Ensures the main() function only runs when the script is executed directly, not when imported as a module.

## How to Use

### Prerequisites
- Python 3.6 or higher (for type hints support)
- Both data.txt and main.py files in the same directory

### Running the Program
1. Open a terminal/command prompt in the project directory
2. Run the following command:
   ```bash
   python main.py
   ```

3. Follow the on-screen prompts:
   - Press Enter when you see "Press Enter to start reading the file..."
   - Read each line displayed on the screen
   - Press Enter after each line to continue to the next line
   - The program will automatically exit when you reach the end of the file

### Example Usage Session
```
Press Enter to start reading the file...
[User presses Enter]
The Lost City of Meridia
Press Enter to read the next line...
[User presses Enter]
Chapter 1: The Beginning
Press Enter to read the next line...
[User presses Enter]
1. In the heart of an ancient civilization lay a city that time had forgotten.
Press Enter to read the next line...
[... continues until end of file ...]
End of file reached.
```

## Technical Details
- **File Format**: Plain text (.txt)
- **Language**: English
- **Content Length**: 100 lines
- **Python Version**: 3.6+
- **Encoding**: UTF-8
- **Design Pattern**: Generator pattern for memory efficiency

## Key Concepts Demonstrated
1. **File I/O** - Reading files using context managers
2. **Generators** - Memory-efficient lazy evaluation
3. **Type Hints** - Type annotations for better code clarity
4. **Exception Handling** - Catching StopIteration for clean program termination
5. **Interactive Programming** - User input handling with input()
6. **System Operations** - Program exit using sys.exit()

## Author Notes
This project combines a complete narrative dataset with a practical Python implementation that demonstrates best practices for file reading, including memory efficiency through generators and clean resource management. It serves as an educational tool for learning Python file I/O operations and generator functions.
