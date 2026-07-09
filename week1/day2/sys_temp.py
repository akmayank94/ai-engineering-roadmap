"""
Day 2 - Understanding System Role and Temperature

This script demonstrates how a System Prompt controls the
behavior of the LLM and how Temperature influences the
creativity and consistency of the generated responses.

Author: Mayank
"""

import os
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
# This client will be used to communicate with the the selected Large Language Model (LLM).
# --------------------------------------------------------
client = Groq(api_key = my_api_key)

# Selecting the language model for response.
model = "llama-3.3-70b-versatile"


role = "user"
prompt = "Suggest me 5 names for my coffee business. Give 2 word answers."


# --------------------------------------------------------
# STEP 3: Define the conversation.
#
# LLMs receive a list of messages.
#
# System Role:
# Defines the assistant's personality, behavior,
# tone, and instructions before responding.
#
# User Role:
# Represents the actual question or request from
# the user.
# --------------------------------------------------------

message_system = {
    "role":"system",
    "content": "You are my grandma who has a tech background."
}
message = {
    "role":role,
    "content":prompt
}

# combine all messages into o conversation.
messages = [message_system, message]


# --------------------------------------------------------
# STEP 4: Generate a response.
#
# Temperature controls randomness.
#
# Temperature = 0
# More factual, consistent and deterministic output.
#
# Temperature = 2
# More creative, diverse and unpredictable output.
# 
# Temerature value ranges from 0 to 2. (Not less then 0 or more than 2, It will give error if set)
#
# Lower temperature is generally preferred for:
# - Coding
# - Q&A
# - Data Extraction
#
# Higher temperature is useful for:
# - Brainstorming
# - Story Writing
# - Creative Ideas
# --------------------------------------------------------
response = client.chat.completions.create(model=model, messages=messages, temperature = 0)


# --------------------------------------------------------
# STEP 5: Extract the assistant's reply
# --------------------------------------------------------
answer = response.choices[0].message.content

# Display the generated response.
print(answer)