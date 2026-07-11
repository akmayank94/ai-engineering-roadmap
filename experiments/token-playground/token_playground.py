"""
==========================================================
TOKEN PLAYGROUND
----------------------------------------------------------
A collection of practical experiments to understand how
Large Language Models use tokens in different situations.

Author : Mayank
==========================================================
"""

import os
from dotenv import load_dotenv
from groq import Groq

# ==========================================================
# Load API Key
# ==========================================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found.")

client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"

# ==========================================================
# Helper Function
# ==========================================================

def print_usage(title, response):
    """
    Prints token statistics in a readable format.
    """

    usage = response.usage

    print("=" * 60)
    print(title)
    print("-" * 60)

    print(f"Prompt Tokens     : {usage.prompt_tokens}")
    print(f"Completion Tokens : {usage.completion_tokens}")
    print(f"Total Tokens      : {usage.total_tokens}")
    print(f"Finish Reason     : {response.choices[0].finish_reason}")
    print()

# ==========================================================
# Experiment 1
# ==========================================================

def experiment_1():
    """
    Short vs Long Prompts
    """

    print("\n\nEXPERIMENT 1")
    print("Question:")
    print("Does prompt length affect token usage?\n")

    prompts = [
        "Hi",
        "Hello",
        "Hello World",
        "Explain AI.",
        "Explain Artificial Intelligence in detail."
    ]

    for prompt in prompts:

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=100
        )

        print_usage(prompt, response)

# ==========================================================
# Experiment 2
# ==========================================================

def experiment_2():
    """
    English vs Hindi vs Hinglish Token Comparison
    """

    print("\n\n")
    print("=" * 70)
    print("EXPERIMENT 2 : English vs Hindi vs Hinglish")
    print("=" * 70)

    print("\nResearch Question:")
    print("Does language affect token usage?\n")

    prompts = [
        ("English", "What is Artificial Intelligence?"),
        ("Hinglish", "Artificial Intelligence kya hota hai?"),
        ("Hindi", "कृत्रिम बुद्धिमत्ता क्या है?"),
        ("English Long", "Explain Artificial Intelligence in simple words."),
        ("Hindi Long", "कृत्रिम बुद्धिमत्ता को सरल शब्दों में समझाइए।"),
    ]

    for language, prompt in prompts:

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=100
        )

        print_usage(f"{language}\nPrompt: {prompt}", response)

# ==========================================================
# Experiment 3
# ==========================================================

def experiment_3():
    """
    Emojis
    """

    pass

# ==========================================================
# Experiment 4
# ==========================================================

def experiment_4():

    pass

# ==========================================================
# Experiment 5
# ==========================================================

def experiment_5():

    pass

# ==========================================================
# Experiment 6
# ==========================================================

def experiment_6():

    pass

# ==========================================================
# Experiment 7
# ==========================================================

def experiment_7():

    pass

# ==========================================================
# Experiment 8
# ==========================================================

def experiment_8():

    pass

# ==========================================================
# Experiment 9
# ==========================================================

def experiment_9():

    pass

# ==========================================================
# Experiment 10
# ==========================================================

def experiment_10():

    pass

# ==========================================================
# Main
# ==========================================================

def main():

    experiment_1()

    experiment_2()
    # experiment_3()
    # experiment_4()
    # experiment_5()
    # experiment_6()
    # experiment_7()
    # experiment_8()
    # experiment_9()
    # experiment_10()


if __name__ == "__main__":
    main()