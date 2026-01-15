import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def ask_llm(question, context):
    """Sends the question and code context to the Groq AI model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Error: Please set GROQ_API_KEY in your .env file."

    # Pattern 2: Context Injection
    prompt = f"""
You are an expert on the ERPNext codebase. Use the following context to answer the question.

## Context
{context}

## Question
{question}

## Instructions
- Base your answer on the provided context
- Cite specific files if mentioned
- If the context doesn't contain the answer, say so
"""

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        return f"AI Error: {str(e)}"