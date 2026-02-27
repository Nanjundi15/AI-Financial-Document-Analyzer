from crewai import Task
from agents import financial_analyst
from tools import read_data_tool


analyze_financial_document_task = Task(
    description="""
Analyze the financial document and answer the query: {query}
""",

    expected_output="Detailed financial analysis",

    agent=financial_analyst,

    tools=[read_data_tool],
)