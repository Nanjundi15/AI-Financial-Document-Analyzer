import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_financial_text(text, query):

    prompt = f"""
You are a financial analyst.

Document:
{text}

User query:
{query}

Provide:

Revenue
Profit
Growth
Risks
Investment recommendation
"""

    response = model.generate_content(prompt)

    return response.text