from langchain_community.utilities import WikipediaAPIWrapper


def main():
    # Initialize wrapper
    wiki_tool = WikipediaAPIWrapper()
    # Conduct a search and return summaries of the top results
    documents = wiki_tool.run("Artificial Intelligence")
    print(documents)


if __name__ == "__main__":
    main()