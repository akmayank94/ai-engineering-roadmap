# 🧠 Week 1 • Day 7 — ReAct (Reasoning + Acting) Fundamentals

> Day 7 introduces **ReAct (Reasoning + Acting)**, one of the foundational reasoning patterns used in modern AI systems.
>
> In this lesson, I built a simple ReAct demonstration in pure Python to understand how Large Language Models can reason, decide when to use external tools, observe their outputs, and continue solving a problem step by step.

---

# 📖 Overview

Large Language Models are trained on historical data and therefore cannot answer questions that require real-time information or external computation on their own.

To overcome this limitation, AI systems provide models with access to external **tools** such as calculators, search engines, databases, APIs, or custom functions.

However, another challenge appears:

> **How does the model know which tool to use, when to use it, and what to do after receiving the tool's result?**

This is where the **ReAct (Reasoning + Acting)** pattern becomes useful.

Instead of trying to solve everything in a single response, the model repeatedly follows a reasoning loop:

- Think about the current task
- Decide which tool is required
- Execute one tool
- Observe the result
- Continue reasoning
- Stop when enough information has been collected

This lesson demonstrates that reasoning cycle using a simple shopping example implemented in Python without relying on AI agent frameworks.

---

> **Learning Milestone**
>
> This implementation is part of **Week 1** of my AI Engineering Roadmap.
>
> The objective is to understand how LLMs interact with external tools before exploring larger AI engineering topics such as AI agents, workflow orchestration, and agent frameworks later in the roadmap.

---

# 🎯 Learning Objectives

During this lesson, I explored:

- What ReAct stands for
- Why LLMs require external tools
- Why single-shot prompting is often insufficient
- How reasoning and tool execution work together
- The Thought → Action → Observation loop
- Building a simple ReAct workflow using Python
- Understanding how modern AI systems perform multi-step reasoning

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Programming Language |
| Groq SDK | LLM API |
| python-dotenv | Environment Variables |
| uv | Package Management |
| Regular Expressions (`re`) | Action Parsing |
| Git | Version Control |
| GitHub | Project Hosting |

---

# 📂 Project Structure

```text
day7/

├── .venv/
├── .env
├── ReAct_chain.py
├── README.md
├── pyproject.toml
└── uv.lock
```

---

# ⚙️ Setup

## Clone Repository

```bash
git clone <repository-url>
```

---

## Navigate to Day 7

```bash
cd week1/day7
```

---

## Create Virtual Environment

```bash
uv venv --python 3.10
```

---

## Activate Environment

### PowerShell

```powershell
.venv\Scripts\activate.ps1
```

### CMD

```cmd
.venv\Scripts\activate.bat
```

---

## Install Dependencies

```bash
uv sync
```

or

```bash
uv add groq python-dotenv
```

---

## Create `.env`

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run

```bash
python ReAct_chain.py
```

---

# 🧠 Key Concepts Covered

During this lesson I learned:

- ReAct Pattern
- Reasoning + Acting
- Tool Calling
- External Function Execution
- Multi-step Reasoning
- Conversation Memory
- Observation Feedback
- Action Parsing
- Prompt-guided Tool Usage
- Iterative Reasoning
- Controlled LLM Workflows

---

# 🤔 Why Single-Shot Prompting Isn't Enough

Many tasks require information that the model cannot generate from its training data alone.

For example:

- Current weather
- Live stock prices
- Calculator operations
- Database queries
- Company-specific information

Trying to solve these tasks using only one prompt often produces inaccurate or incomplete responses.

Instead, the model should:

1. Understand the problem.
2. Decide what information is missing.
3. Use an appropriate tool.
4. Continue reasoning using the tool's output.
5. Produce the final answer.

This iterative reasoning process is the foundation of the ReAct pattern.

---

# 🔄 ReAct Workflow

The reasoning loop implemented in this lesson follows this sequence:

```text
User Question
      │
      ▼
LLM Thinks
      │
      ▼
Choose One Tool
      │
      ▼
Execute Tool
      │
      ▼
Receive Observation
      │
      ▼
Reason Again
      │
      ▼
Need Another Tool?
      │
 ┌────┴─────┐
 │          │
Yes        No
 │          │
 ▼          ▼
Repeat   Final Answer
```

---

# ⚙️ How This Demonstration Works

This implementation follows a simplified ReAct workflow.

### Step 1

The user asks a question.

Example:

```text
I have 5000 rupees.
What is the price of an iPhone 17,
and how much money will I have left?
```

---

### Step 2

The model reasons about what information is required.

```text
Thought:
I need the price of the product.
```

---

### Step 3

The model chooses one available tool.

```text
Action:
get_product_price("iPhone 17")
```

---

### Step 4

Python executes the selected function.

```text
Observation:
1000
```

---

### Step 5

The observation is added back into the conversation.

The model now has additional information and continues reasoning.

---

### Step 6

The model decides another calculation is required.

```text
Action:
calculator("5000 - 1000")
```

---

### Step 7

The calculator returns:

```text
4000
```

---

### Step 8

Since all required information has been collected, the model produces the final answer.

---

# 🧪 Practical Observations

During experimentation, I observed:

- The model cannot execute Python functions by itself.
- The system prompt instructs the model how tools should be used.
- Only one tool should be executed at a time.
- Tool outputs become observations for the next reasoning step.
- Conversation history allows the model to continue reasoning across multiple iterations.
- The loop terminates once the model produces a Final Answer.

---

# 💡 Why This Lesson Matters

Modern AI applications often need to interact with external systems.

Examples include:

- Weather APIs
- Search engines
- SQL databases
- Vector databases
- Payment systems
- Email services
- Calculators

The ReAct pattern provides a structured way for LLMs to decide when these tools should be used while keeping the reasoning process transparent and iterative.

Understanding this reasoning pattern makes it easier to understand how many modern AI frameworks coordinate LLMs with external tools.

---

# ⚠️ Challenges Faced

During implementation I encountered several practical challenges:

- Missing `python-dotenv` dependency
- Designing a prompt that forces the model to call only one tool at a time
- Parsing tool calls using Regular Expressions
- Passing observations back into the conversation history
- Determining when the reasoning loop should terminate

Each challenge demonstrated an important aspect of building reliable LLM workflows.

---

# 🚀 Next Steps

The concepts learned in this lesson provide the foundation for more advanced AI engineering topics.

Upcoming topics include:

- AI Agents
- Workflow orchestration
- LangChain
- LangGraph
- Multi-tool workflows
- Memory systems
- Retrieval-Augmented Generation (RAG)

---

# 🎤 Interview Questions & Answers

### 1. What does ReAct stand for?

ReAct stands for **Reasoning + Acting**.

It is a prompting pattern where an LLM alternates between reasoning about a problem and performing actions (tool calls) until enough information has been gathered to produce a final answer.

---

### 2. Why do LLMs need external tools?

LLMs are trained on historical datasets and cannot directly access live information or execute external operations.

Tools extend an LLM's capabilities by allowing it to perform calculations, query APIs, retrieve database records, or access real-time information.

---

### 3. What is the Thought → Action → Observation loop?

It is the core reasoning cycle used in ReAct.

- **Thought** – Decide what information is needed.
- **Action** – Execute one tool.
- **Observation** – Receive the tool's output.
- Repeat until enough information has been collected.

---

### 4. Why shouldn't multiple tools be executed at once?

Executing one tool at a time keeps reasoning sequential and allows each observation to influence the next decision.

This reduces errors and makes the reasoning process easier to understand and debug.

---

### 5. What is an Observation?

An Observation is the result returned by a tool.

The observation becomes new information that is added back into the conversation so the model can continue reasoning.

---

### 6. Why is conversation history important?

Conversation history allows the model to remember previous thoughts, actions, and observations.

Without memory, the model would repeatedly solve the same problem from the beginning.

---

### 7. Why is the system prompt important?

The system prompt defines:

- Available tools
- Tool usage rules
- Output format
- Reasoning behavior
- When the model should stop

Without clear instructions, the model may generate invalid or inconsistent tool calls.

---

### 8. How is ReAct different from a normal prompt?

A normal prompt expects one response.

ReAct allows the model to solve problems through multiple reasoning steps, using tools whenever necessary before producing the final answer.

---

### 9. Is this implementation a complete AI agent?

No.

This project demonstrates the **ReAct reasoning pattern**, which is one of the foundational ideas behind many modern AI agent systems.

A complete AI agent typically includes additional capabilities such as dynamic tool selection, memory management, planning, error recovery, and workflow orchestration.

---

# 🔑 Key Takeaway

ReAct teaches that solving complex problems is often an iterative process rather than a single response.

By combining reasoning with external tool usage, LLMs can tackle tasks that would otherwise be difficult or impossible using their training data alone.

Understanding this reasoning pattern provides a strong foundation for learning more advanced AI engineering concepts in the upcoming weeks.

---

## 👨‍💻 Author

**Mayank**

This practical implementation is part of my **AI Engineering Roadmap**, where I document my learning journey through practical experiments, hands-on coding, and implementation of fundamental AI engineering concepts.

Each lesson builds upon the previous one, gradually progressing from LLM fundamentals toward more advanced AI workflows and production-oriented engineering practices.