"""
Week 1 • Day 7 - ReAct (Reasoning + Acting)

This implementation demonstrates the ReAct reasoning pattern, where a Large
Language Model (LLM) alternates between reasoning and tool execution to solve
a problem step by step.

Instead of answering everything in a single response, the model follows an
iterative workflow:

Thought → Action → Observation → Repeat → Final Answer

The purpose of this exercise is to understand how LLMs interact with external
tools before moving on to more advanced AI engineering concepts.
"""

import os
import re
from time import sleep

from dotenv import load_dotenv
from groq import Groq

# ----------------------------------------------------------
# Load environment variables
# ----------------------------------------------------------

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found. Please check your .env file.")

# ----------------------------------------------------------
# Initialize Groq client
# ----------------------------------------------------------

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

# ----------------------------------------------------------
# Tool Definitions
#
# These Python functions act as external tools that the LLM
# can request during the reasoning process.
# ----------------------------------------------------------


def get_product_price(product):
    """
    Returns the price of a requested product.
    """

    if product == "iPhone 17":
        return 1000

    elif product == "iPhone 15":
        return 500

    return 0


def calculator(expression):
    """
    Evaluates a mathematical expression.

    This simulates a calculator tool that the LLM can call
    whenever numerical computation is required.
    """

    try:
        return eval(expression)

    except Exception:
        return "Calculation Error"


# ----------------------------------------------------------
# Register Available Tools
#
# The model cannot execute Python functions directly.
# Instead, it generates an Action, and the program maps
# that action to one of these registered tools.
# ----------------------------------------------------------

tools = {
    "get_product_price": get_product_price,
    "calculator": calculator
}

# ----------------------------------------------------------
# System Prompt
#
# This prompt teaches the model:
#
# • Which tools are available
# • How tool calls should be formatted
# • That only one tool should be called at a time
# • To wait for observations before continuing
# • When to stop reasoning and return the final answer
# ----------------------------------------------------------

system_prompt = """
You are a shopping assistant.

You have these tools:

get_product_price(product)
calculator(expression)

IMPORTANT:

Call tools exactly like these examples:

Action: get_product_price("iPhone 17")
Action: calculator("5000 - 1000")

Never write:

get_product_price(product="iPhone 17")

Never write:

calculator(expression="5000 - 1000")

Follow these rules:

1. Decide what you need to do next.
2. Call ONLY ONE tool at a time.
3. After writing an Action, STOP immediately.
4. Never guess or invent a tool result.
5. Wait until you receive an Observation.
6. Then decide your next action.
7. When the task is complete, give the Final Answer.

Format:

Thought: what you need to do

Action: tool_name(argument)

When finished:

Final Answer: your answer
"""


# ----------------------------------------------------------
# ReAct Reasoning Loop
#
# This function implements the complete Thought → Action →
# Observation cycle until the model reaches a Final Answer.
# ----------------------------------------------------------

def run_agent(question):
    """
    Executes a ReAct reasoning workflow.

    Steps:

    1. Send the user's question to the LLM.
    2. Allow the model to reason.
    3. Detect whether a tool should be executed.
    4. Execute the requested tool.
    5. Return the tool's output as an Observation.
    6. Repeat until the model produces a Final Answer.
    """

    # Conversation memory shared with the LLM
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]

    # Prevent infinite reasoning loops
    for step in range(5):

        print("\n------------------")
        print("STEP", step + 1)
        print("------------------")

        # Generate the next reasoning step
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )

        answer = response.choices[0].message.content

        print(answer)

        # Stop once the model produces a Final Answer
        if "Final Answer:" in answer:
            break

        # --------------------------------------------------
        # Extract the requested tool call from the model's
        # response using Regular Expressions.
        #
        # Example:
        #
        # Action: calculator("5000 - 1000")
        # --------------------------------------------------

        match = re.search(
            r"Action:\s*(\w+)\((.*?)\)",
            answer
        )

        if match:

            tool_name = match.group(1)

            tool_input = match.group(2)

            # Remove unnecessary spaces and quotation marks
            tool_input = tool_input.strip()
            tool_input = tool_input.strip('"')

            # ----------------------------------------------
            # Execute the requested tool.
            #
            # If the tool exists, call the corresponding
            # Python function.
            # ----------------------------------------------

            if tool_name in tools:

                tool = tools[tool_name]

                observation = tool(tool_input)

            else:

                observation = "Tool not found"

            print("Observation:", observation)

            # ----------------------------------------------
            # Store the LLM's reasoning in conversation
            # history so future reasoning has context.
            # ----------------------------------------------

            messages.append({
                "role": "assistant",
                "content": answer
            })

            # ----------------------------------------------
            # Return the tool's output back to the LLM.
            #
            # This Observation becomes the input for the
            # next reasoning iteration.
            # ----------------------------------------------

            messages.append({
                "role": "user",
                "content": "Observation: " + str(observation)
            })

            # Small delay to make each reasoning step
            # easier to observe during execution.
            sleep(5)


# ----------------------------------------------------------
# User Query
#
# This is the task given to the model.
# The ReAct loop will continue until enough information
# has been gathered to answer it completely.
# ----------------------------------------------------------

prompt = """
I have 5000 rupees.

What is the price of an iPhone 17?

And how much money will I have left?
"""

run_agent(prompt)

"""
TERMINAL OUTPUT:
(day7) PS D:\CUDA projects\Practice\AI Engineer Roadmap\week1\day7> python .\ReAct_chain.py

------------------
STEP 1
------------------
Thought: To find out how much money will be left after buying an iPhone 17, I first need to know the price of the iPhone 17.

Action: get_product_price("iPhone 17")
Observation: 1000

------------------
STEP 2
------------------
Thought: Now that I know the price of the iPhone 17 is 1000 rupees, I can calculate how much money will be left after buying it by subtracting the price from the initial amount of money.

Action: calculator("5000 - 1000")
Observation: 4000

------------------
STEP 3
------------------
Thought: I now have all the necessary information: the price of the iPhone 17 is 1000 rupees, and after buying it, I will have 4000 rupees left.

Final Answer: The price of the iPhone 17 is 1000 rupees, and I will have 4000 rupees left.
"""