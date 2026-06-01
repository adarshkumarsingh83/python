import asyncio
from fastmcp import tools
from mcp.client.sse import sse_client
from mcp import ClientSession

class McpClient:

    async def execute(self):
        async with sse_client('http://localhost:8000/sse') as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print('Session initialized')

                tool_list = await session.list_tools()
                print('Tools:', tool_list)
                for tool in tool_list:
                   print(f'{tool.name}: {tool.description }')

                tool_name = input('Enter tool name to execute: ')
                a = int(input('Enter first number: '))
                b = int(input('Enter second number: ')) 

                result = await session.execute_tool(tool_name, a, b)
                print('Result:', result)

    async def fetchResource(self):
        async with sse_client('http://localhost:8000/sse') as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print('Session initialized')

                result = await session.read_resource('resource://data.json')
                print('Fetched Resource:', result)
    
