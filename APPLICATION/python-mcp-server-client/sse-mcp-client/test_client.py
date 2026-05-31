"""
Test client to validate McpClient functionality without server
"""
import asyncio
from services.McpClient import McpClient

async def test_client_instantiation():
    """Test that McpClient can be instantiated"""
    print("✓ Test 1: Testing McpClient instantiation...")
    try:
        client = McpClient()
        print("  ✓ McpClient instantiated successfully")
        print(f"  ✓ Client object: {client}")
        print(f"  ✓ Available methods: {[m for m in dir(client) if not m.startswith('_')]}")
        return True
    except Exception as e:
        print(f"  ✗ Failed to instantiate: {e}")
        return False

async def test_client_methods():
    """Test that McpClient has required methods"""
    print("\n✓ Test 2: Testing McpClient methods exist...")
    try:
        client = McpClient()
        
        # Check if methods exist
        assert hasattr(client, 'execute'), "execute method not found"
        assert hasattr(client, 'fetchResource'), "fetchResource method not found"
        
        print("  ✓ execute() method exists")
        print("  ✓ fetchResource() method exists")
        
        # Check if they're coroutines
        assert asyncio.iscoroutinefunction(client.execute), "execute is not async"
        assert asyncio.iscoroutinefunction(client.fetchResource), "fetchResource is not async"
        
        print("  ✓ execute() is async coroutine")
        print("  ✓ fetchResource() is async coroutine")
        return True
    except Exception as e:
        print(f"  ✗ Method check failed: {e}")
        return False

async def test_imports():
    """Test that all required imports work"""
    print("\n✓ Test 3: Testing imports...")
    try:
        from fastmcp import tools
        from mcp.client.sse import sse_client
        from mcp import ClientSession
        import asyncio
        
        print("  ✓ fastmcp imported successfully")
        print("  ✓ mcp.client.sse imported successfully")
        print("  ✓ ClientSession imported successfully")
        print("  ✓ asyncio imported successfully")
        return True
    except ImportError as e:
        print(f"  ✗ Import failed: {e}")
        return False

async def main():
    print("=" * 60)
    print("MCP CLIENT TEST SUITE")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(await test_imports())
    results.append(await test_client_instantiation())
    results.append(await test_client_methods())
    
    # Summary
    print("\n" + "=" * 60)
    print(f"RESULTS: {sum(results)}/{len(results)} tests passed")
    print("=" * 60)
    
    if all(results):
        print("\n✓ All tests PASSED! Client is ready for server connection.")
        print("\nNote: To test with server:")
        print("  1. Ensure the MCP server is running")
        print("  2. Verify server is listening on http://localhost:8000/sse")
        print("  3. Run: python main.py")
    else:
        print("\n✗ Some tests FAILED. Please fix the issues above.")

if __name__ == "__main__":
    asyncio.run(main())
