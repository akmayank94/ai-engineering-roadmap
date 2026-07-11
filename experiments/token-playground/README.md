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

| Experiment | Status |
|------------|--------|
| 1. Prompt Length vs Tokens | ✅ |
| 2. English vs Hindi vs Hinglish | ✅ |
| 3. Emojis & Special Characters | ⏳ |
| 4. Punctuation Impact | ⏳ |
| 5. max_tokens Comparison | ⏳ |
| 6. Temperature vs Tokens | ⏳ |
| 7. System Prompt Overhead | ⏳ |
| 8. Conversation History Growth | ⏳ |
| 9. Safety Responses | ⏳ |
| 10. Token Cost Calculator | ⏳ |

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

# 🚀 Future Improvements

- Token usage graphs
- Automatic Markdown report generation
- CSV export
- Cost estimation calculator
- Model comparison
- Performance benchmarking

---

## 👨‍💻 Author

**Mayank**

Part of my **AI Engineering Roadmap**, where I explore AI concepts through practical experiments, real-world implementations, and detailed technical documentation.