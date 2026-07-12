# 🔬 Token Playground

> A collection of practical experiments to understand how Large Language Models (LLMs) process tokens under different conditions.

---

# 📖 Overview

This project explores one of the most fundamental concepts in AI Engineering — **Tokens**.

Instead of only learning the theory behind tokenization, this project performs hands-on experiments to observe how different prompts, languages, emojis, punctuation, response limits, and conversation history affect token usage.

The goal is to better understand how token consumption influences:

- API Cost
- Context Window
- Response Length
- Performance
- Production Scalability

---

# 🎯 Objectives

- Understand how LLMs tokenize text.
- Compare token usage across different languages.
- Observe the impact of prompt length.
- Study production concepts such as `max_tokens` and `finish_reason`.
- Build practical intuition about LLM cost optimization.

---

# 🛠 Technologies

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Programming Language |
| Groq SDK | LLM API |
| python-dotenv | Environment Variables |
| uv | Package Management |

---

# 📂 Project Structure

```text
token-playground/

├── token_playground.py
├── README.md
├── results.md
└── observations.md
```

---

# 🧪 Experiments

# 🧪 Experiments

| Experiment | Description | Status |
|------------|-------------|--------|
| 1. Prompt Length vs Token Usage | Observe how prompt length affects token consumption. | ✅ |
| 2. English vs Hindi vs Hinglish | Compare multilingual tokenization efficiency. | ✅ |
| 3. Emojis & Unicode | Measure the impact of emojis and Unicode characters on token usage. | ✅ |
| 4. Punctuation Impact | Study how punctuation influences tokenization. | ✅ |
| 5. Temperature vs Creativity | Analyze whether temperature changes token usage or only creativity. | ✅ |
| 6. System Prompt Overhead | Measure additional prompt tokens introduced by system prompts. | ✅ |
| 7. Conversation History Growth | Observe how conversation memory increases prompt tokens. | ✅ |
| 8. Safety Behaviour | Analyze how LLMs respond to unsafe prompts. | ✅ |

---

# 💡 Why This Project?

Understanding token usage is one of the most practical skills in AI Engineering.

Efficient token management helps developers:

- Reduce API costs
- Improve response speed
- Optimize prompt design
- Build scalable AI systems

Rather than relying only on theoretical explanations, this project records real experimental observations using actual LLM API responses.

---

# 📚 Key Learnings

Throughout these experiments, several important observations emerged:

- Tokenization is based on tokenizer vocabulary rather than character count.
- Prompt length directly influences prompt token usage.
- Different languages consume different numbers of tokens.
- Emojis and Unicode characters introduce additional prompt tokens.
- Temperature changes creativity without affecting prompt token count.
- System prompts increase the overall prompt size.
- Conversation history continually increases API cost.
- Modern LLMs usually refuse unsafe requests while still returning a normal completion.

These experiments transformed theoretical concepts into measurable observations through practical testing.

---

## 👨‍💻 Author

**Mayank**

Part of my **AI Engineering Roadmap**, where I explore AI concepts through practical experiments, real-world implementations, and detailed technical documentation.