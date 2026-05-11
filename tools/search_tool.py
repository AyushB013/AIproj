
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
load_dotenv()
search = GoogleSerperAPIWrapper()
def search_web(query):
    return search.run(query)