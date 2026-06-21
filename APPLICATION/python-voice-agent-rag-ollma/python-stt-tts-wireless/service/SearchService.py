import logging

from config import AppConfig

logger = logging.getLogger(__name__)


class SearchService:

    def __init__(self, app_config: AppConfig):
        self.app_config = app_config
        self.collection = self.app_config.getCollection()
        self.load_data(
            self.app_config.get_data(),
            self.app_config.get_metadatas(),
            self.app_config.get_ids(),
        )

    def load_data(self, data: list, metadatas: list, ids: list):
        logger.info("Loading data into Chroma DB collection...")
        logger.info("Data: %s", data)
        logger.info("Metadatas: %s", metadatas)
        logger.info("IDs: %s", ids)
        self.collection.add(
            documents=data, metadatas=metadatas, ids=ids
        )

    def search(self, query: str, top_k: int = 1) -> list:
        results = self.collection.query(
            query_texts=[query], n_results=top_k
        )
        return results["documents"]