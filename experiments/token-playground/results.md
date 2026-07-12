# 📊 Token Playground Results

This document records the raw outputs obtained from each experiment.

---

# Experiment 1

## Research Question

Does prompt length affect token usage?

| Prompt | Prompt Tokens | Completion Tokens | Total Tokens | Finish Reason |
|---------|--------------:|------------------:|-------------:|---------------|
| Hi | 36 | 24 | 60 | stop |
| Hello | 36 | 25 | 61 | stop |
| Hello World | 37 | 25 | 62 | stop |
| Explain AI. | 39 | 100 | 139 | length |
| Explain Artificial Intelligence in detail. | 42 | 100 | 142 | length |

---

# Experiment 2

## Research Question

Does language affect token usage?

| Language | Prompt Tokens | Completion Tokens | Total Tokens | Finish Reason |
|----------|--------------:|------------------:|-------------:|---------------|
| English | 40 | 100 | 140 | length |
| Hinglish | 44 | 100 | 144 | length |
| Hindi | 51 | 100 | 151 | length |
| English Long | 43 | 100 | 143 | length |
| Hindi Long | 59 | 100 | 159 | length |

---

# Experiment 3

## Research Question

Do emojis and Unicode characters increase token usage?

| Prompt | Prompt Tokens | Completion Tokens | Total Tokens | Finish Reason |
|---------|--------------:|------------------:|-------------:|---------------|
| Hello | 36 | 25 | 61 | stop |
| Hello 😊 | 38 | 25 | 63 | stop |
| Hello 😊😊😊 | 42 | 25 | 67 | stop |
| Hello ❤️ | 38 | 25 | 63 | stop |
| Hello 🚀🚀🚀 | 45 | 25 | 70 | stop |
| 🔥 AI Engineering 🚀 | 43 | 100 | 143 | length |

---

# Experiment 4

## Research Question

Does punctuation affect token usage?

| Prompt | Prompt Tokens | Completion Tokens | Total Tokens | Finish Reason |
|---------|--------------:|------------------:|-------------:|---------------|
| Hello | 36 | 25 | 61 | stop |
| Hello. | 37 | 25 | 62 | stop |
| Hello... | 37 | 25 | 62 | stop |
| Hello!!!!! | 37 | 25 | 62 | stop |
| Hello???? | 37 | 25 | 62 | stop |
| Hello?!?!?! | 39 | 25 | 64 | stop |

---

# Experiment 5

## Research Question

Does temperature affect creativity and token usage?

| Temperature | Prompt Tokens | Completion Tokens | Finish Reason |
|------------:|--------------:|------------------:|---------------|
| 0.0 | 44 | 100 | length |
| 0.3 | 44 | 100 | length |
| 0.7 | 44 | 100 | length |
| 1.0 | 44 | 100 | length |
| 2.0 | 44 | 100 | length |

> Response content became progressively more creative as the temperature increased, while prompt token usage remained unchanged.

---

# Experiment 6

## Research Question

Does adding a system prompt increase prompt token usage?

| System Prompt | Prompt Tokens |
|---------------|--------------:|
| None | 43 |
| CEO | 50 |
| Comedian | 49 |
| Lawyer | 49 |
| Grandma | 49 |

---

# Experiment 7

## Research Question

How does conversation history affect prompt token usage?

| Conversation | Prompt Tokens | Completion Tokens | Total Tokens |
|-------------|--------------:|------------------:|-------------:|
| Multi-message conversation | 82 | 11 | 93 |

---

# Experiment 8

## Research Question

How do LLMs respond to unsafe requests?

Three different unsafe prompts were tested.

### Common Results

| Observation | Result |
|------------|--------|
| finish_reason | stop |
| Model Behaviour | Refused harmful request |
| Alternative Guidance | Provided safe information |