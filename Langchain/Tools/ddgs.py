from langchain_community.tools import DuckDuckGoSearchResults

searcgh_tool = DuckDuckGoSearchResults()

result = searcgh_tool.invoke("Demon slayer anime box office collection")

print(result)