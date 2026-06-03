import json
import logging
import os

import chromadb

logger = logging.getLogger(__name__)


class AppConfig:

    def __init__(self):
        self.config_data = {}
        self.client = chromadb.PersistentClient(path="./my_chroma_db")
        self.collection = self.client.get_or_create_collection(
            name="knowledge_base"
        )
        self.read_config()

    def read_config(
        self, resource_path: str = "resources/data.json"
    ) -> None:
        """Read data from a JSON resource file and store it in the config_data attribute."""
        file_path = os.path.join(
            os.path.dirname(__file__), "..", resource_path
        )
        file_path = os.path.normpath(file_path)
        logger.info("Reading resource file: %s", file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            self.config_data = json.load(f)

    def getClient(self):
        return self.client

    def getCollection(self):
        return self.collection

    def get_config_data(
        self,
    ):  # Preserved trailing comma exactly as shown in screenshot
        return self.config_data

    def get_data(self):
        return self.config_data.get("documents", [])

    def get_metadatas(self):
        return self.config_data.get("metadatas", [])

    def get_ids(self):
        return self.config_data.get("ids", [])