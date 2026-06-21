from repository import DataRepository
import logging

class DataService:
    __logger = logging.getLogger(__name__)

    @staticmethod
    def insert_data(data: dict) -> str:
        DataService.__logger.info(f"Service layer: Inserting data: {data}")
        return DataRepository.insert_data(data)

    @staticmethod
    def get_data_by_id(data_id: str) -> dict:
        DataService.__logger.info(f"Service layer: Retrieving data by id: {data_id}")
        return DataRepository.get_data_by_id(data_id)

    @staticmethod
    def get_all_data() -> list:
        DataService.__logger.info("Service layer: Retrieving all data")
        return DataRepository.get_all_data()

    @staticmethod
    def update_data(data_id: str, updated_data: dict) -> bool:
        DataService.__logger.info(f"Service layer: Updating data with id: {data_id} and updated data: {updated_data}")
        return DataRepository.update_data(data_id, updated_data)

    @staticmethod
    def delete_data(data_id: str) -> bool:
        DataService.__logger.info(f"Service layer: Deleting data with id: {data_id}")
        return DataRepository.delete_data(data_id)