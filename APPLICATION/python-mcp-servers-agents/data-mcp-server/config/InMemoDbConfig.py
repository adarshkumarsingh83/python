import mongomock
import logging 

class InMemoDbConfig:
    __logger = logging.getLogger(__name__)
    __inMemoDbClient = mongomock.MongoClient()
    __db = __inMemoDbClient['in_memory_db']
    __collection = __db['in_memory_collection']

    @staticmethod
    def get_in_memo_db_client():
        InMemoDbConfig.__logger.info("Returning In-Memory MongoDB Client instance")
        return InMemoDbConfig.__inMemoDbClient

    @staticmethod
    def get_db():
        InMemoDbConfig.__logger.info("Returning In-Memory MongoDB instance")
        return InMemoDbConfig.__db

    @staticmethod
    def get_collection():
        InMemoDbConfig.__logger.info("Returning In-Memory MongoDB collection instance")
        return InMemoDbConfig.__collection