import logging
import os 
import config.AppConfig as AppConfig
from starlette.requests import Request
from starlette.responses import PlainTextResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = AppConfig.getMcp()

@mcp.custom_route("/admin/info", methods=["GET"])
async def app_info(request: Request) -> PlainTextResponse:
    """Returns information about the application."""
    logger.info("Received request for application info")
    app_name = os.getenv("APP_NAME", "My MCP Application")
    app_version = os.getenv("APP_VERSION", "1.0.0")
    info = f"{app_name} - Version {app_version}"
    logger.info(f"Returning application info: {info}")
    return PlainTextResponse(info)

@mcp.custom_route("/admin/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    """Returns the health status of the application."""
    logger.info("Received request for health check")
    return PlainTextResponse("Application is healthy.")

@mcp.custom_route("/user/info", methods=["GET"])
async def user_info(request: Request) -> PlainTextResponse:
    """Returns information about the user."""
    logger.info("Received request for user info")
    return PlainTextResponse("User information goes here.")


@mcp.resource("resource://{fileName}")
def get_resource(fileName: str) -> str:
    """Returns the contents of a resource file."""
    logger.info(f"Received request for resource: {fileName}")
    try:
        file_path = os.path.join(os.getcwd(),"resources", fileName)
        logger.info(f"Looking for resource at: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            logger.info(f"Successfully read resource: {fileName}")
            return content
    except FileNotFoundError:
        logger.error(f"Resource not found: {fileName}")
        return "Error: Resource not found."