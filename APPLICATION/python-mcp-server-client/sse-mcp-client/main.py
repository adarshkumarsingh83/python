
from services.McpClient import McpClient
import asyncio

async def main():
    client = McpClient()
    await client.execute()
    await client.fetchResource()
    

if __name__ == "__main__":
    asyncio.run(main())