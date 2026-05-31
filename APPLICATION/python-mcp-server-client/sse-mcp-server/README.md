# Project Title

## Installation

To install the required dependencies, run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

To start the MCP server:

```bash
source venv/bin/activate
python main.py
```

## Tools Available

The MCP server provides the following tools:

1. **add_numbers** - Adds two numbers together.
   - Parameters: `a` (int), `b` (int)
   - Returns: Sum as string

2. **subtract_numbers** - Subtracts the second number from the first.
   - Parameters: `a` (int), `b` (int)
   - Returns: Difference as string

3. **multiply_numbers** - Multiplies two numbers together.
   - Parameters: `a` (int), `b` (int)
   - Returns: Product as string

4. **divide_numbers** - Divides the first number by the second.
   - Parameters: `a` (int), `b` (int)
   - Returns: Quotient as string (handles division by zero)

5. **compare_numbers** - Compares two numbers and returns which one is greater.
   - Parameters: `a` (int), `b` (int)
   - Returns: Comparison result as string

## API Endpoints

- `GET /admin/info` - Returns application information
- `GET /admin/health` - Returns health status
- `GET /user/info` - Returns user information

## Resources

- `resource://{fileName}` - Returns the contents of a file in the `resources/` directory

## Testing

To run the tests for all tools:

```bash
source venv/bin/activate
python test.py
```

All tools have been tested and are working correctly.