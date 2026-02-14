import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_tasks(goal, users, constraints, template_type):

    prompt = f"""
You are a senior product manager and software architect.

Generate:
1. User stories
2. Engineering tasks grouped by frontend/backend/db
3. Risks and unknowns

Goal:
{goal}

Users:
{users}

Constraints:
{constraints}

Template:
{template_type}

Output in clean Markdown format.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
