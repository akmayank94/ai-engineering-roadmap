# 🚀 Day 1 - Your First LLM API Call

> Learn how to connect a Python application to a Large Language Model (LLM) using the Groq API, securely manage API keys with environment variables, and generate your first AI response.

---

## 📖 Overview

This is the first Implementation in my **AI Engineering Roadmap**.

The goal of this Implementation is to understand the complete workflow of making an LLM API call using Python. Instead of using ChatGPT through a web browser, we interact directly with a language model through code.

By the end of this Implementation, you'll understand how modern AI applications communicate with LLMs and how to securely manage API keys.

---

# 🎯 Learning Objectives

After completing this Implementation, you should be able to:

- Create a Python Implementation using **uv**
- Create and activate a virtual environment
- Install third-party Python packages
- Securely store API keys using `.env`
- Read environment variables in Python
- Initialize the Groq client
- Send your first prompt to an LLM
- Receive and display the model's response

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Programming Language |
| uv | Python Implementation & Package Manager |
| Groq SDK | Communicate with LLMs |
| python-dotenv | Load environment variables |
| Git | Version Control |
| GitHub | Code Hosting |

---

# 📂 Implementation Structure

```text
day1/

├── .venv/
├── .env
├── .gitignore
├── .python-version
├── hello_llm.py
├── main.py
├── pyImplementation.toml
├── uv.lock
└── README.md
```

### File Description

| File | Description |
|------|-------------|
| hello_llm.py | Main application that communicates with the LLM |
| pyImplementation.toml | Implementation configuration and dependencies |
| uv.lock | Locked dependency versions |
| .python-version | Python version used in this Implementation |
| .env | Stores the API key securely *(not pushed to GitHub)* |
| README.md | Implementation documentation |

---

# ⚙️ Setup Instructions

## 1. Clone the Repository

```bash
git clone <repository-url>
```

---

## 2. Navigate to Day 1

```bash
cd week1/day1
```

---

## 3. Create Virtual Environment

```bash
uv venv --python 3.10
```

---

## 4. Activate Virtual Environment

### PowerShell

```powershell
.venv\Scripts\activate.ps1
```

### CMD

```cmd
.venv\Scripts\activate.bat
```

---

## 5. Install Dependencies

```bash
uv sync
```

> If `uv.lock` is not available:

```bash
uv add groq python-dotenv
```

---

## 6. Create a `.env` File

Create a file named **`.env`**

```env
GROQ_API_KEY=your_api_key_here
```

---

## 7. Run the Program

```bash
python hello_llm.py
```

---

# 💻 Sample Output

```text
Who is Cristiano Ronaldo?

Cristiano Ronaldo is a Portuguese professional footballer widely regarded as one of the greatest football players of all time...
```

> The output may differ because LLM responses are generated dynamically.

---

# 🧠 Concepts Learned

During this Implementation I learned:

- What an LLM API is
- Why developers use APIs instead of ChatGPT UI
- What a Virtual Environment is
- Why package isolation matters
- How `uv` simplifies Python development
- Why API keys should never be hardcoded
- How `.env` files work
- How environment variables are loaded
- How to initialize the Groq client
- The structure of an LLM request
- The structure of an LLM response

---

# 🔍 Understanding the Workflow

```
 User Prompt
      │
      ▼
Python Program
      │
      ▼
  Groq SDK
      │
      ▼
  Groq API
      │
      ▼
 LLM Model
      │
      ▼
Generated Response
      │
      ▼
Print Output
```

---

# ⚠️ Common Errors

## ❌ API Key Not Found

```
ValueError: GROQ_API_KEY not found.
```

### Solution

- Check your `.env` file.
- Ensure the variable name is:

```env
GROQ_API_KEY=your_api_key
```

---

## ❌ Invalid Model Name

```
404 Model Not Found
```

### Solution

Verify that:

- The model name is correct.
- Your account has access to that model.

---

## ❌ Module Not Found

```
ModuleNotFoundError
```

### Solution

Install the required packages.

```bash
uv sync
```

or

```bash
uv add groq python-dotenv
```

---

# 💡 Best Practices Followed

- ✅ Used a virtual environment
- ✅ Stored API key in `.env`
- ✅ Did not hardcode secrets
- ✅ Used dependency management with `uv`
- ✅ Kept Implementation isolated
- ✅ Added Implementation documentation

---

# 🚀 What's Next?

In the next lesson, I'll explore:

- Multiple Messages
- System Prompts
- Temperature
- Prompt Engineering Fundamentals

---

# 📚 References

- Groq Python SDK Documentation
- Python Dotenv Documentation
- Python Official Documentation

---

## 👨‍💻 Author

**Mayank**

This Implementation is part of my **AI Engineering Roadmap**, where I'm learning AI Engineering by building practical Implementations, documenting concepts, and sharing everything publicly on GitHub.

If you found this Implementation helpful, consider ⭐ starring the repository.

---
