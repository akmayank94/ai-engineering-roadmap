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