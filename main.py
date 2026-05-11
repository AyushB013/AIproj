import yaml
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from tools.search_tool import search_web
load_dotenv()
llm = ChatOllama(model="phi3")
# load agent configs
with open("agents/web_searcher.yaml","r") as f: summary_agent = yaml.safe_load(f)
with open("agents/summerizer.yaml","r") as f: summary_agent = yaml.safe_load(f)
# load task
with open("tasks/tasks.yaml", "r") as f: tasks = yaml.safe_load(f)
task = tasks["research_task"] ["description"]
#search web
web_results = search_web(task)
#summarize
prompt = f"""
Role: {summary_agent['role']}
Goal: {summary_agent['goal']}
Backstory: {summary_agent['backstory']}
Web Results: {web_results}
Summarize this information clearly.
"""
response = llm.invoke(prompt)
print(response.content)