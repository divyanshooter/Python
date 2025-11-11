from langchain_openai import ChatOpenAI
from langchain.tools import tool
from ddgs import DDGS
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI()

prompt=hub.pull('hwchase17/react')

search_tool=DuckDuckGoSearchRun()

# with DDGS() as search_tool:
#     results = search_tool.text("top India news today", max_results=5)
#     print(results)

agent=create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

agent_executor=AgentExecutor(agent=agent,tools=[search_tool],verbose=True)
response =agent_executor.invoke({"input":"3 ways to reach goa from delhi"})
print(response['output'])
