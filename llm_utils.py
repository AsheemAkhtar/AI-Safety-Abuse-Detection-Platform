from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def explain_risk(text, risk_score):

    prompt = f"""
You are an AI Trust & Safety analyst assistant.

Analyze the following message.

MESSAGE:
{text}

RISK SCORE:
{risk_score:.2f}

Return analysis in EXACT markdown format.

# Risk Summary
One short sentence.

# Risk Indicators
- Bullet point
- Bullet point
- Bullet point

# Abuse Category
- One category

# Recommended Action
- One action
- One action

Keep response concise, professional, and visually clean.
Avoid long paragraphs.
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content