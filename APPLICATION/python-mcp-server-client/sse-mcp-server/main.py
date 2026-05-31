import config.AppConfig as AppConfig

mcp = AppConfig.getMcp()

def executeMcpServer():
    print("Starting MCP Server...")
    mcp.run(transport="sse",)

if __name__ == "__main__":
    executeMcpServer()