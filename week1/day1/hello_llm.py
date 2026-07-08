"""
Day 1 - Your First LLM API Call

This script demonstrates how to send a prompt to an LLM
using the Groq Python SDK and receive a response.

Author: Mayank
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# --------------------------------------------------------
# STEP 1: Load environment variables from the .env file
# This keeps sensitive information like API keys outside the source code.
# --------------------------------------------------------
load_dotenv()


# Retrieve the API key from environment variables.
my_api_key = os.getenv("GROQ_API_KEY")


# Stop execution if the API key is missing.
if not my_api_key:
    raise ValueError ("GROQ_API_KEY not found. Please check your .env file.")



# --------------------------------------------------------
# STEP 2: Create the Groq client
# This client will be used to communicate with the LLM.
# --------------------------------------------------------
client = Groq(api_key = my_api_key)

# Selecting the language model for response.
model = "llama-3.3-70b-versatile"


role = "user"
prompt = "Who is Cristiano Ronaldo?"


# --------------------------------------------------------
# STEP 3: Create the conversation
# Every LLM request is sent as a list of messages.
# Each message contains:
#   - role
#   - content
# --------------------------------------------------------
message = {
    "role":role,
    "content":prompt
}

messages = [message]

response = client.chat.completions.create(model=model, messages=messages)



# --------------------------------------------------------
# STEP 4: Extract the assistant's reply
# --------------------------------------------------------
answer = response.choices[0].message.content
print(answer)
