# 📄 Resume Screening Application (Version 1.0)

> An AI-powered Resume Screening application that extracts structured information from resumes and job descriptions using Large Language Models (LLMs), validates the output with Pydantic, compares candidate skills against job requirements, and generates screening reports.
> Version 1.0 supports resumes and job requirements in txt format, pdf and docs support will be in version 2.0
---

# 📖 Overview

Recruiters often spend significant time manually reviewing resumes to determine whether a candidate matches a job description.

This application automates the first stage of that process by:

- Extracting structured information from resumes
- Extracting structured information from job descriptions
- Validating the extracted data using Pydantic
- Comparing candidate skills with job requirements
- Generating a match percentage
- Producing screening reports in JSON and text formats

Instead of relying on fragile string parsing, the application uses **JSON Mode** and **Pydantic schemas** to ensure reliable structured outputs from the LLM.

---

# 🎯 Objectives

This application was built to understand and practice:

- Structured Outputs from LLMs
- JSON Mode
- Pydantic Schema Validation
- Prompt Engineering for Data Extraction
- Converting unstructured text into structured Python objects
- Building simple AI-powered automation workflows
- Separating AI extraction from business logic

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Programming Language |
| Groq SDK | LLM API |
| Pydantic | Data Validation |
| JSON | Structured Output |
| python-dotenv | Environment Variables |
| uv | Package Management |
| Git | Version Control |
| GitHub | Project Hosting |

---

# 📂 Project Structure

```text
resume-screening/

├── .venv/
├── data/
│   ├── resume.txt
│   └── job_description.txt
│
├── outputs/
│   ├── screening_report.json
│   └── screening_report.txt
│
├── schema.py
├── resume_screening.py
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

## Navigate to the Project

```bash
cd applications/resume-screening
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
uv add groq python-dotenv pydantic
```

---

## Create `.env`

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run

```bash
python resume_screening.py
```

---

# 🧠 Concepts Learned

During this application I learned:

- JSON Mode
- Structured Outputs
- Pydantic Models
- Schema Validation
- Prompt Engineering
- Information Extraction
- Business Logic Separation
- Skill Matching
- AI-powered Resume Parsing

---

# 🔄 Application Workflow

```text
Resume.txt
        │
        ▼
LLM Extraction
        │
        ▼
Resume Object (Pydantic)
        │
        │
Job Description.txt
        │
        ▼
LLM Extraction
        │
        ▼
Job Description Object (Pydantic)
        │
        ▼
Python Matching Logic
        │
        ▼
Match Percentage
        │
        ▼
Recommendation
        │
        ▼
JSON Report + Text Report
```

---

# 🏗️ Architecture

The application intentionally separates responsibilities into independent stages.

### 1. Resume Extraction

The resume is passed to the LLM with a predefined Pydantic schema.

The model returns only valid JSON.

The JSON is validated before being converted into a Python object.

---

### 2. Job Description Extraction

The same reusable extraction function is used for the job description.

Using a generic extraction function removes duplicate code and makes the application easier to extend.

---

### 3. Skill Comparison

The matching logic is implemented in Python instead of asking the LLM to calculate a score.

This approach makes the application:

- deterministic
- easier to debug
- cheaper to run
- more reliable

---

### 4. Report Generation

The final result is exported as:

- `screening_report.json`
- `screening_report.txt`

This makes the application suitable for further automation or integration.

---

# 📊 Matching Strategy

The application uses a simple weighted scoring approach.

### Required Skills

Weight: **70%**

These skills are considered essential for the role.

---

### Preferred Skills

Weight: **30%**

These skills improve the candidate's profile but are not mandatory.

---

### Recommendation Rules

| Match Percentage | Recommendation |
|-----------------|----------------|
| 80% or higher | Shortlist for Interview |
| 60–79% | Consider for Interview |
| Below 60% | Reject |

---

# 📄 Example Output

```text
========================================
RESUME SCREENING REPORT
========================================

Candidate

Mayank

----------------------------------------

Match Percentage

70%

----------------------------------------

Matched Skills

✓ Python
✓ SQL
✓ Git
✓ Machine Learning

----------------------------------------

Missing Skills

✗ Docker
✗ AWS
✗ FastAPI

----------------------------------------

Recommendation

Consider for Interview
```

---

# 💡 Why Pydantic?

Without Pydantic, an LLM may return inconsistent text formats.

Using Pydantic ensures:

- required fields exist
- data types are correct
- validation happens automatically
- downstream code receives predictable objects

This greatly simplifies AI application development.

---

# 🚀 Future Improvements

Planned enhancements include:

- Support PDF resumes
- Support DOCX resumes
- Compare candidate experience
- Compare education requirements
- Match projects and certifications
- Export PDF reports
- Batch screening of multiple resumes
- Web interface for recruiters

---

# 🔑 Key Takeaway

Building AI applications is not just about calling an LLM.

Reliable AI systems combine:

- Structured prompts
- JSON outputs
- Schema validation
- Business logic
- Automation

This application demonstrates how these components work together to transform unstructured text into actionable information.

---

## 👨‍💻 Author

**Mayank**

This application is part of my **AI Engineering Roadmap**, where I document my journey of learning AI Engineering by building practical applications, conducting experiments, and understanding the engineering principles behind modern AI systems. Each milestone focuses on implementing concepts from scratch while keeping the solutions simple, reusable, and production-oriented.
