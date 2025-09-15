# To install: pip install tavily-python
import os
from dotenv import load_dotenv

load_dotenv()

from tavily import TavilyClient

client = TavilyClient(os.getenv("TAVILY_API_KEY"))
response = client.search(query="")
print(response)
