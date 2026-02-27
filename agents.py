import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from tools import read_data_tool

llm = LLM(
    model="gpt-4o-mini",
    temperature=0.2
)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and provide insights based on {query}",
    verbose=True,
    backstory="Expert financial analyst",
    tools=[read_data_tool],
    llm=llm,
    allow_delegation=False
)