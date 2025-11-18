import os
from google.generativeai import GenerativeModel, configure
from models.db import cursor

# Load Gemini API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
cur, conn = cursor()

# Configure the API
configure(api_key=GEMINI_API_KEY)

# Create model with example context
model = GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="You are Medify-AI pharmacy assistant. Keep replies concise (20–30 words). The prices are in Rs. and stock in Units. Do not mention price/ stock unless asked. Use only relevant medical emojis, and use them sparingly. For casual greetings, reply politely within 15 words. Always stay pharmacy-focused. And use both data + context window to check for prices/stock of medicines. Strictly use english."
)

cur.execute("""SELECT * FROM medicines;""")
medicines = cur.fetchall()

def ask_llm(message: str, context_window: dict = None) -> str:
    """
    Takes a message string, sends it to Gemini, and returns the response text.
    """

    memory_text = f"The store has following medicine data: {medicines}, this is your context window: {context_window}. answer my question w.r.t this data and context window. ignore everything else."

    message = message + memory_text
    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage (disable in production)
if __name__ == "__main__":
    print(ask_llm("list all medicines in stock"))