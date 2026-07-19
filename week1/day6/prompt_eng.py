"""
Day 6 - Prompt Engineering Fundamentals

This exercise demonstrates how prompt design influences the quality,
consistency, and reliability of Large Language Model (LLM) responses.

The goal is to progressively improve a prompt using six production-oriented
components commonly used in real AI applications.

Concepts Covered:
1. Role
2. Task
3. Constraints
4. Output Format
5. Zero-shot / One-shot / Few-shot Examples
6. Fallback Instructions

Key Learning:
Well-structured prompts reduce ambiguity, improve consistency,
and make AI systems significantly more reliable in production.
"""

import os

from dotenv import load_dotenv
from groq import Groq

# ----------------------------------------------------------
# Load environment variables
# ----------------------------------------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API KEY NOT FOUND. Please check your .env file.")

# ----------------------------------------------------------
# Initialize Groq client
# ----------------------------------------------------------

client = Groq(api_key=api_key)

model = "llama-3.3-70b-versatile"

# ----------------------------------------------------------
# Utility function for sending prompts to the LLM
# ----------------------------------------------------------


def llm_ans(prompt):
    """
    Sends a prompt to the language model and returns
    the generated response.
    """

    message = {
        "role": "user",
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    answer = response.choices[0].message.content

    return answer


# ----------------------------------------------------------
# Production-Oriented Prompt
#
# Prompt Anatomy:
# 1. Role
# 2. Task
# 3. Constraints
# 4. Output Format
# 5. One-shot Example
# 6. Fallback
# ----------------------------------------------------------

prompt = """
# Role
You are a support assistant at a mobile/laptop company.

# Task
Classify each customer complaint into a single category.

# Constraints
The complaint must belong to ONLY one of the following categories:

- Billing
- Technical
- Return

# Output Format
Return exactly ONE word.

Allowed outputs:

Billing
Technical
Return
Other

# One-shot Example

Complaint:
I want a refund for my order.

Answer:
Return

# Fallback

If the complaint does not belong to any of the available
categories, return:

Other

Customer Complaint:

My Marriage is not working
"""

print(llm_ans(prompt))