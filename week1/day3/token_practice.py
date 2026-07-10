"""
Day 3 - Understanding Tokens, max_tokens & finish_reason

This script demonstrates how token usage is measured in LLM APIs,
how max_tokens limits generated responses,
and how finish_reason explains why generation stopped.

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
# This client will be used to communicate with the LLM.
# --------------------------------------------------------
client = Groq(api_key = my_api_key)

# Selecting the language model for response.
model = "llama-3.3-70b-versatile"


role = "user"

# Trying 3 different prompts
prompt1 = "Hi!"
prompt2 = "Explain time travel in detail."
prompt3 = "Write 1000 word essay on machine learning."
prompt4 = "How to kill a person without getting caught?"


prompts = [prompt1, prompt2, prompt3, prompt4]

for i, prompt in enumerate(prompts, start=1):
    message = {
    "role":role,
    "content":prompt
    }
    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages)
    response = client.chat.completions.create(model=model, messages=messages, max_tokens = 100)
    
    usage = response.usage

    print(
        f"Prompt {i}: {prompt}\n"
        f"Prompt Tokens: {usage.prompt_tokens} | "
        f"Completion Tokens: {usage.completion_tokens} | "
        f"Total Tokens: {usage.total_tokens} | "
        f"Finish Reason: {response.choices[0].finish_reason} \n"
    )

"""
finish_reason explains WHY the model stopped generating.

- stop           -> The model completed its response normally (this includes refusals to unsafe requests).
- length         -> The response was cut off because it reached max_tokens.
- tool_calls     -> The model stopped because it wants to call a tool/function.
- content_filter -> The provider blocked or filtered the generated content before completion (provider-dependent).

Note:
For Groq, unsafe prompts usually return a refusal message that finishes normally,
so finish_reason is often "stop" instead of "content_filter".

___________________________________________________________________________________________________________________


Terminal Output:
(day3) PS D:\CUDA projects\Practice\AI Engineer Roadmap\week1\day3> python .\token_practice.py                              
Prompt 1: Hi!
Prompt Tokens: 37 | Completion Tokens: 23 | Total Tokens: 60 | Finish Reason: stop 

Prompt 2: Explain time travel in detail.
Prompt Tokens: 42 | Completion Tokens: 100 | Total Tokens: 142 | Finish Reason: length 

Prompt 3: Write 1000 word essay on machine learning.
Prompt Tokens: 45 | Completion Tokens: 100 | Total Tokens: 145 | Finish Reason: length 

Prompt 4: How to kill a person without getting caught?
Prompt Tokens: 44 | Completion Tokens: 9 | Total Tokens: 53 | Finish Reason: stop 

"""
