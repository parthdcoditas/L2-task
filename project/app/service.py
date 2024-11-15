import os
from dotenv import load_dotenv
from groq import Groq
import requests

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def rewrite_text(text, tone, temperature):
    prompt = f"""
    You are a text rewriting expert. I want you to rephrase the given sentence in the specific {tone} provided.

    Here's an example of how to rewrite in different tones:

    Input: "You need to improve your work performance."
    Output:
    - Formal: "Enhancing your work performance would be beneficial for your professional growth and overall contributions to the team."
    - Casual: "Hey, it'd be awesome if you could work on boosting your performance a bit!"
    - Motivational: "You've got great potential! With a little extra focus, your performance could really shine and take you to the next level!"

    Please rephrase only the given sentence in the specified tone. Do not answer the sentence or add any new information.

    Do not mention the tone in the rewrited response generated and remove the "\n" if they exist.
    Query - {text}
    """

    chat_completion = client.chat.completions.create(
            messages=[
            {'role': 'user', 'content': prompt}
        ],
            model="mixtral-8x7b-32768",
            temperature=temperature
        )
    return chat_completion.choices[0].message.content.strip()

    # if chat_completion.status_code == 200:
    #     return chat_completion.choices[0].message.content.strip()
    #     # return chat_completion.get("rewritten_text")
    # else:
    #     return f"Error: {chat_completion.status_code} - {chat_completion.text}"

