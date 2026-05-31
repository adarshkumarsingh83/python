from config.InMemoDbConfig import InMemoDbConfig
import logging 
from bson import ObjectId
import json 

class DataRepository:
    __logger = logging.getLogger(__name__)
    __collection = InMemoDbConfig.get_collection()

    @staticmethod
    def insert_data(data: dict)-> str:
        DataRepository.__logger.info(f"Inserting data: {data}")
        try:
            result = DataRepository.__collection.insert_one(data)
            return str(result.inserted_id)
        except Exception as e:
            DataRepository.__logger.error(f"Error inserting data: {e}")
            return 'exception generated while inserting data'
        
    @staticmethod
    def get_data_by_id(data_id: str) -> dict:
        DataRepository.__logger.info(f"Retrieving data by id: {data_id}")
        try:
            result = DataRepository.__collection.find_one({"_id": ObjectId(data_id)})
            if result:
                return json.loads(json.dumps(result, default=str))
            else:
                return {}
        except Exception as e:
            DataRepository.__logger.error(f"Error retrieving data by id: {e}")
            return {}
        
    @staticmethod
    def get_all_data() -> list:
        DataRepository.__logger.info("Retrieving all data")
        try:
            results = DataRepository.__collection.find()
            return [json.loads(json.dumps(result, default=str)) for result in results]
        except Exception as e:
            DataRepository.__logger.error(f"Error retrieving all data: {e}")
            return []
        
    @staticmethod
    def update_data(data_id: str, updated_data: dict) -> bool:
        DataRepository.__logger.info(f"Updating data with id: {data_id} and updated data: {updated_data}")
        try:
            result = DataRepository.__collection.update_one({"_id": ObjectId(data_id)}, {"$set": updated_data})
            return result.modified_count > 0
        except Exception as e:
            DataRepository.__logger.error(f"Error updating data: {e}")
            return False
        
    @staticmethod
    def delete_data(data_id: str) -> bool:
        DataRepository.__logger.info(f"Deleting data with id: {data_id}")
        try:
            result = DataRepository.__collection.delete_one({"_id": ObjectId(data_id)})
            return result.deleted_count > 0
        except Exception as e:
            DataRepository.__logger.error(f"Error deleting data: {e}")
            return False