import config.AppConfig as AppConfig

mcp = AppConfig.getMcp()

def executeMcpServer():
    mcp.run(transport="sse")
    print("Starting MCP Server...")

if __name__ == "__main__":
    executeMcpServer()