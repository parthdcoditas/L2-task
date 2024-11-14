import os
from dotenv import load_dotenv
from groq import Groq
import requests

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def rewrite_text(text, tone, temperature=0.7):
    prompt =  """ Hi who is indian prime minister """

    chat_completion = client.chat.completions.create(
            messages=[
            {'role': 'user', 'content': prompt}
        ],
            model="mixtral-8x7b-32768",
            temperature=0.7
        )
    return chat_completion.choices[0].message.content.strip()

    # if chat_completion.status_code == 200:
    #     return chat_completion.choices[0].message.content.strip()
    #     # return chat_completion.get("rewritten_text")
    # else:
    #     return f"Error: {chat_completion.status_code} - {chat_completion.text}"
text = "Please rewrite this text in a more formal tone."
tone = "formal"
print(rewrite_text(text, tone))
