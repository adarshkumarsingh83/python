import logging

from config import AppConfig

logger = logging.getLogger(__name__)


class SearchService:

    def __init__(self, app_config: AppConfig):
        self.app_config = app_config
        self.collection = self.app_config.getCollection()
        self.openai_client = self.app_config.get_openAi_client()
        try:
            self.load_data(
                self.app_config.get_data(),
                self.app_config.get_metadatas(),
                self.app_config.get_ids(),
            )
        except Exception as e:
            logger.warning("Failed to load data during initialization: %s", e)

    def load_data(self, data: list, metadatas: list, ids: list):
        logger.info("Loading data into Chroma DB collection...")
        logger.info("Data: %s", data)
        logger.info("Metadatas: %s", metadatas)
        logger.info("IDs: %s", ids)

        embeddings: list = []
        for index, document in enumerate(data):
            logger.info(
                "Creating embedding for document %d/%d",
                index + 1,
                len(data),
            )
            response = self.openai_client.embeddings.create(
                input=document, model="llama3.1:8b"
            )
            embeddings.append(response.data[0].embedding)

        self.collection.add(
            documents=data,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

    def search(self, query: str, top_k: int = 1) -> list:
        q_emb = (
            self.openai_client.embeddings.create(
                model="llama3.1:8b", input=query
            )
            .data[0]
            .embedding
        )
        results = self.collection.query(
            query_embeddings=[q_emb], n_results=top_k
        )
        return results["documents"][0]