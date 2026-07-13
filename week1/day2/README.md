# 🚀 Day 2 - Understanding System Role & Temperature

> Learn how **System Prompts** control the behavior of a Large Language Model (LLM) and how **Temperature** influences the creativity and consistency of AI-generated responses.

---

# 📖 Overview

In Day 2, we explored two of the most important concepts in Prompt Engineering:

- **System Role**
- **Temperature**

Instead of simply sending a prompt to an LLM, we now provide additional instructions that define **how the AI should behave** before answering.

We also learned how changing the **temperature** parameter affects the randomness and creativity of the generated response.

These concepts are fundamental in building reliable AI-powered applications.

---

# 🎯 Learning Objectives

After completing this implementation, you should be able to:

- Understand the purpose of System Prompts
- Differentiate between System and User messages
- Control an LLM's personality and behavior
- Understand what Temperature means
- Generate deterministic and creative responses
- Choose appropriate temperature values for different use cases

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Programming Language |
| uv | Python implementation & Package Manager |
| Groq SDK | LLM API Communication |
| python-dotenv | Environment Variables |
| Git | Version Control |
| GitHub | Code Hosting |

---

# 📂 implementation Structure

```text
day2/

├── .venv/
├── .env
├── .gitignore
├── .python-version
├── sys_temp.py
├── main.py
├── pyimplementation.toml
├── uv.lock
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone the Repository

```bash
git clone <repository-url>
```

---

## 2️⃣ Navigate to Day 2

```bash
cd week1/day2
```

---

## 3️⃣ Create a Virtual Environment

```bash
uv venv --python 3.10
```

---

## 4️⃣ Activate the Environment

### PowerShell

```powershell
.venv\Scripts\activate.ps1
```

### CMD

```cmd
.venv\Scripts\activate.bat
```

---

## 5️⃣ Install Dependencies

```bash
uv sync
```

or

```bash
uv add groq python-dotenv
```

---

## 6️⃣ Create a `.env` File

```env
GROQ_API_KEY=your_api_key_here
```

---

## 7️⃣ Run the Program

```bash
python sys_temp.py
```

---

# 💻 Sample Output

```text
1. Morning Brew
2. Coffee Lab
3. Bean Scene
4. Java Hub
5. Roast House
```

Running the program again may produce different results depending on the **temperature** value used.

---

# 🧠 Concepts Learned

During this implementation I learned:

- What a System Prompt is
- Difference between System and User roles
- How AI follows instructions before answering
- What Temperature means
- Difference between deterministic and creative outputs
- Why Prompt Engineering is important
- How multiple messages are sent to an LLM
- How LLM behavior can be customized without changing the model

---

# 🧩 Understanding the Conversation Structure

Every conversation sent to an LLM is simply a list of messages.

```python
[
    {
        "role": "system",
        "content": "You are my grandma who has a tech background."
    },
    {
        "role": "user",
        "content": "Suggest me 5 names for my coffee business."
    }
]
```

---

# 🎭 Understanding Message Roles

## 🟢 System Role

The **System Role** defines how the AI should behave throughout the conversation.

Examples:

- Friendly Teacher
- Coding Assistant
- Travel Guide
- Fitness Coach
- Grandma with Tech Background

Think of it as assigning a personality or job to the AI before it starts answering.

---

## 🔵 User Role

The **User Role** contains the actual request or question.

Example:

```text
Suggest me 5 names for my coffee business.
```

The model answers this request while following the System Prompt.

---

# 🌡️ Understanding Temperature

Temperature controls how random or creative the model's responses are.

## Temperature = 0

- Very consistent
- Predictable
- Best for factual tasks
- Great for coding
- Similar output every run

Example Uses

- Programming
- Math
- Question Answering
- Data Extraction

---

## Temperature = 1

- Balanced creativity
- Natural conversations
- General-purpose assistants

---

## Temperature = 2

- Highly creative
- More diverse responses
- Less predictable

Example Uses

- Story Writing
- Poetry
- Marketing Ideas
- Brainstorming

---

# 📊 Temperature Comparison

| Temperature | Output Style | Best For |
|--------------|--------------|-----------|
| **0.0** | Consistent | Coding, Q&A |
| **0.3 - 0.7** | Balanced | Chatbots |
| **1.0** | Creative | Writing |
| **2.0** | Highly Creative | Brainstorming |

---

# 🧪 My Experiment

### Prompt Used

```text
Suggest me 5 names for my coffee business.
Give 2 word answers.
```

### System Prompt

```text
You are my grandma who has a tech background.
```

### Observation

When using a **low temperature**, the generated business names remained relatively consistent.

Increasing the temperature produced more diverse and creative suggestions.

Even though the user prompt remained the same, changing only the **temperature** changed the style of the generated output.

---

# 🔍 Understanding the Workflow

```
User Prompt
        │
        ▼
System Prompt
        │
        ▼
Temperature
        │
        ▼
Groq API
        │
        ▼
LLM
        │
        ▼
Generated Response
```

---

# ⚠️ Common Errors

## API Key Missing

```text
ValueError: GROQ_API_KEY not found
```

### Solution

Check your `.env` file.

---

## Invalid Model Name

```text
404 Model Not Found
```

### Solution

Verify the model name.

---

## Missing Dependencies

```text
ModuleNotFoundError
```

### Solution

Run

```bash
uv sync
```

or

```bash
uv add groq python-dotenv
```

---

# 💡 Best Practices Followed

- ✅ Used Virtual Environment
- ✅ Stored API Keys securely
- ✅ Used Environment Variables
- ✅ Added a System Prompt
- ✅ Used Temperature Parameter
- ✅ Documented the code
- ✅ Kept implementation modular

---

# 🎤 Interview Questions

### Q1. What is the purpose of a System Prompt?

A System Prompt defines the assistant's behavior, personality, and instructions before the user message is processed.

---

### Q2. What does Temperature control?

Temperature controls the randomness and creativity of the generated output.

---

### Q3. Which temperature is recommended for coding tasks?

Temperature **0** because it produces more consistent and deterministic responses.

---

### Q4. Why use System Prompts?

They help ensure the AI consistently behaves according to the desired role or context without modifying the user prompt.

---

# 🚀 What's Next?

In the next lesson, I'll continue exploring Prompt Engineering and learn more techniques for controlling and improving LLM responses.

---

# 📚 References

- Groq Python SDK Documentation
- Python Dotenv Documentation
- Prompt Engineering Concepts
- Python Official Documentation

---

## 👨‍💻 Author

**Mayank**

This implementation is part of my **AI Engineering Roadmap**, where I'm learning AI Engineering by building practical implementations, documenting concepts, experimenting with modern LLMs, and sharing everything publicly on GitHub.

If you found this implementation helpful, consider ⭐ starring the repository.
