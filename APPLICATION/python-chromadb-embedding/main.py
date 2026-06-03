import logging

from config import AppConfig
from service import SearchService

logger = logging.getLogger(__name__)


def main():
    app_config = AppConfig()
    search_service = SearchService(app_config)

    query = "What is Chroma DB used for?"
    results = search_service.search(query)
    logger.info("Search results for query %r: %s", query, results)
    print("Search results:", results)
    for i, doc in enumerate(results, start=1):
        print(f"{i}. {doc}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()