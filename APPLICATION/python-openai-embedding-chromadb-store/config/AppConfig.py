import json
import logging
import os

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

logger = logging.getLogger(__name__)


class AppConfig:

    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Add it to a .env file or set it as an environment variable."
            )

        self.config_data = {}
        self.client = chromadb.PersistentClient(path="./db/my_chroma_db")
        self.collection = self.client.get_or_create_collection(
            name="knowledge_base"
        )
        self.openAi_client = OpenAI(base_url="http://localhost:11434/v1", api_key=api_key)
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

    def get_config_data(self,):
        return self.config_data

    def get_openAi_client(self):
        return self.openAi_client

    def get_data(self):
        return self.config_data.get("documents", [])

    def get_metadatas(self):
        return self.config_data.get("metadatas", [])

    def get_ids(self):
        return self.config_data.get("ids", [])