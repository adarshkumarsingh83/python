from config import AppMcpConfig
from service import DataService
import logging

logger = logging.getLogger(__name__)
mcpServer = AppMcpConfig.get_mcp_server()

def initializeTools():
    logger.info("Initializing tools...")

@mcpServer.tool(name="insert_data", description="Insert data into the database")
def insert_data(data: dict) -> str:
    logger.info(f"Tool layer: Inserting data: {data}")
    return DataService.insert_data(data)

@mcpServer.tool(name="get_data_by_id", description="Retrieve data by ID from the database")
def get_data_by_id(data_id: str) -> dict:
    logger.info(f"Tool layer: Retrieving data by id: {data_id}")
    return DataService.get_data_by_id(data_id)

@mcpServer.tool(name="get_all_data", description="Retrieve all data from the database")
def get_all_data() -> list:
    logger.info("Tool layer: Retrieving all data")
    return DataService.get_all_data()

@mcpServer.tool(name="update_data", description="Update data in the database by ID")
def update_data(data_id: str, updated_data: dict) -> bool:
    logger.info(f"Tool layer: Updating data with id: {data_id} and updated data: {updated_data}")
    return DataService.update_data(data_id, updated_data)

@mcpServer.tool(name="delete_data", description="Delete data from the database by ID")
def delete_data(data_id: str) -> bool:
    logger.info(f"Tool layer: Deleting data with id: {data_id}")
    return DataService.delete_data(data_id)

