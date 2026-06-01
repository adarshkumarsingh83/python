# SSE MCP Client

A Python MCP (Model Context Protocol) client implementation using Server-Sent Events (SSE).

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Navigate to Project

Navigate to the project directory:

```bash
cd sse-mcp-client
```

### Step 2: Create a Virtual Environment (Recommended)

It's recommended to create a virtual environment to isolate project dependencies:

```bash
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

### Step 4: Install Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install:
- **fastmcp**: A fast MCP implementation for Python
- **mcp**: Model Context Protocol library
- **httpx**: HTTP client library
- And all other dependencies

### Step 5: Verify Installation

To verify the installation was successful:

```bash
pip list | grep -E "fastmcp|mcp|httpx"
```

You should see fastmcp and related packages in the list.

## Running the Client

### Option 1: Test Client (No Server Required)

To verify the client code is working correctly without a running server:

```bash
python test_client.py
```

This will run a comprehensive test suite that validates:
- ✓ All imports are working
- ✓ McpClient can be instantiated
- ✓ Methods are properly defined as async coroutines

**Expected Output:**
```
============================================================
MCP CLIENT TEST SUITE
============================================================
✓ Test 3: Testing imports...
✓ Test 1: Testing McpClient instantiation...
✓ Test 2: Testing McpClient methods exist...
============================================================
RESULTS: 3/3 tests passed
============================================================
```

### Option 2: Run Main Client (Requires Running Server)

To run the main client and connect to the MCP server:

```bash
python main.py
```

**Prerequisites:**
- The MCP server must be running on `http://localhost:8000/sse`
- If the server is on a different URL/port, update the URL in `services/McpClient.py`

**What the client does:**
1. Connects to the SSE server at `http://localhost:8000/sse`
2. Initializes the session
3. Lists available tools from the server
4. Prompts you to enter:
   - Tool name to execute
   - First number
   - Second number
5. Executes the tool and displays results
6. Fetches and displays resources from `resource://data.json`

### Step-by-Step: Run Complete Application

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Test the client first (no server needed)
python test_client.py

# 3. In another terminal, start the MCP server
cd ../sse-mcp-server
source venv/bin/activate
python main.py

# 4. Back in the client terminal, run the main client
cd ../sse-mcp-client
python main.py
```

## Project Structure

```
sse-mcp-client/
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── test_client.py         # Client test suite
├── README.md              # This file
├── venv/                  # Virtual environment (created after setup)
└── services/
    └── McpClient.py       # MCP client implementation
```

## Troubleshooting

### Issue: Connection Error When Running main.py

**Error:** `httpcore.ConnectError: All connection attempts failed`

**Solution:**
1. Ensure the MCP server is running on `http://localhost:8000/sse`
2. Check server configuration in `../sse-mcp-server/config/AppConfig.py`
3. Verify the URL in `services/McpClient.py` matches the server endpoint

### Issue: Module Not Found

**Error:** `ModuleNotFoundError: No module named 'fastmcp'`

**Solution:**
1. Ensure virtual environment is activated: `source venv/bin/activate`
2. Reinstall dependencies: `pip install -r requirements.txt`

### Issue: Permission Denied

**Error:** `Permission denied` when activating venv

**Solution:**
- macOS/Linux: Run `chmod +x venv/bin/activate`
- Windows: Run terminal as Administrator

### Issue: Python Not Found

**Error:** `python: command not found`

**Solution:**
- Use `python3` instead of `python`
- Check Python is installed: `python3 --version`

## Configuration

The client connects to the MCP server at `http://localhost:8000/sse`.

To change the server URL, edit `services/McpClient.py`:

```python
# Change this line:
async with sse_client('http://localhost:8000/sse') as (read, write):
# To your desired endpoint, e.g.:
async with sse_client('http://your-server:8080/sse') as (read, write):
```

## Usage Example

After the client connects and initializes:

```
Session initialized
Tools: [...]
Enter tool name to execute: add
Enter first number: 5
Enter second number: 3
Result: 8
Fetched Resource: {...}
```

## Requirements

- fastmcp >= 3.2.4
- mcp >= 1.24.0
- httpx >= 0.28.1
- python-dotenv >= 1.1.0
- And other dependencies listed in `requirements.txt`

See `requirements.txt` for the complete list.

## Development

To add more functionality to the client:

1. Edit `services/McpClient.py` to add new methods
2. Update `main.py` to call new methods
3. Run tests: `python test_client.py`

## Contributing

Contributions are welcome! Please ensure all tests pass before submitting changes:

```bash
python test_client.py
```

## License

Specify your license here.

