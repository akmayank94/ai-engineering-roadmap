# 📄 Day 5 - AI Resume Parser & Candidate Ranking System

> Build an end-to-end AI-powered resume screening pipeline that parses resumes from PDF/DOCX files, extracts structured information using Large Language Models, compares candidates against a job description, and ranks applicants based on AI-generated matching scores.

---

# 📖 Overview

Recruiters often spend hours manually reviewing resumes to identify suitable candidates for a role.

In this project, I built an AI-powered Resume Screening System that automates this workflow using Large Language Models (LLMs).

The application:

- Reads resumes from PDF and DOCX files
- Extracts structured information using Pydantic
- Parses job descriptions into structured JSON
- Compares each candidate against the job description
- Generates AI-based match scores
- Produces hiring verdicts
- Ranks candidates from best to worst

This project combines all the concepts learned throughout Week 1 into a single end-to-end application.

---

# 🎯 Learning Objectives

By completing this project I learned how to:

- Parse PDF resumes
- Parse Microsoft Word resumes
- Build reusable Pydantic schemas
- Extract structured information from unstructured documents
- Use JSON Mode for reliable AI outputs
- Compare structured Resume and Job Description objects
- Generate AI-powered hiring recommendations
- Process multiple resumes automatically
- Rank candidates using AI-generated scores

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Programming Language |
| Groq SDK | LLM API |
| Pydantic | Data Validation |
| JSON Mode | Structured Outputs |
| python-dotenv | Environment Variables |
| PyPDF | Read PDF resumes |
| python-docx | Read DOCX resumes |
| uv | Package Management |
| Git | Version Control |
| GitHub | Project Hosting |

---

# 📂 Project Structure

```text
day5/

├── .venv/
├── resumes/
│   ├── resume01.pdf
│   ├── resume02.docx
│   ├── resume03.pdf
│   └── resume04.docx
│
├── resume_parser.py
├── README.md
├── pyproject.toml
├── uv.lock
└── .python-version
```

---

# ⚙️ Setup

## Clone Repository

```bash
git clone <repository-url>
```

---

## Navigate to Day 5

```bash
cd week1/day5
```

---

## Create Virtual Environment

```bash
uv venv --python 3.10
```

---

## Activate Environment

PowerShell

```powershell
.venv\Scripts\activate.ps1
```

CMD

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
uv add groq python-dotenv pydantic pypdf python-docx
```

---

## Create `.env`

```env
GROQ_API_KEY=your_api_key_here
```

---

## Add Resume Files

Place all resumes inside the `resumes` folder.

Supported formats:

- PDF
- DOCX

---

## Run

```bash
python resume_parser.py
```

---

# 🧠 Concepts Learned

This project combines everything learned in Week 1:

- LLM API Calls
- System Prompts
- JSON Mode
- Structured Outputs
- Pydantic Models
- Temperature = 0
- Resume Parsing
- Job Description Parsing
- PDF Processing
- DOCX Processing
- AI-based Candidate Evaluation

---

# 🔄 Application Workflow

```text
Job Description
        │
        ▼
LLM Extraction
        │
        ▼
Structured Job Object
        │
        │
        │
Resume Folder
        │
        ▼
Read PDF / DOCX
        │
        ▼
Resume Text
        │
        ▼
LLM Resume Parser
        │
        ▼
Structured Resume Object
        │
        ▼
AI Resume Matcher
        │
        ▼
Match Score
        │
        ▼
Hiring Verdict
        │
        ▼
Rank All Candidates
```

---

# 🏗️ Project Architecture

The application is divided into four independent stages.

---

## 1. Job Description Parsing

The job description is first converted into a structured Pydantic object containing:

- Role
- Required Skills
- Preferred Skills
- Education Requirements
- Experience
- Responsibilities

---

## 2. Resume Parsing

Each resume is automatically read based on its file type.

Supported formats:

- PDF
- DOCX

The extracted text is passed to the LLM, which converts it into a structured Resume object.

---

## 3. Candidate Matching

Instead of comparing raw text, the application compares two structured objects:

- Job Description
- Resume

The LLM evaluates:

- Matching skills
- Missing skills
- Experience
- Overall suitability

It then generates a structured hiring result.

---

## 4. Candidate Ranking

Every resume receives a match score.

Candidates are sorted from highest to lowest score, allowing recruiters to quickly identify the strongest applicants.

---

# 📊 Example Output

```text
Processing: resume01.pdf
Score: 70

Processing: resume02.docx
Score: 60

Processing: resume03.pdf
Score: 60

Processing: resume04.docx
Score: 40
```

---

## Top Candidates

```text
Ashish Raj
Score: 70%

Priyanshu Singh
Score: 60%
```

---

## Lowest Candidates

```text
Abhay Pratap Singh
Score: 60%

Anshit Verma
Score: 40%
```

---

# 💡 Why Structured Outputs?

Traditional AI applications often return plain text that is difficult to process automatically.

Using:

- JSON Mode
- Pydantic

ensures every LLM response follows a predictable structure, making it easier to build reliable AI applications.

---

# ⚠️ Challenges Faced

While building this project, I encountered several common development issues:

- Missing Python packages (`python-dotenv`, `pypdf`, `python-docx`)
- Missing imports (`BaseModel`, `Path`, `time`)
- Incorrect variable names (`message` vs `messages`)
- Understanding the difference between Python standard library modules and installable packages

Resolving these issues helped reinforce debugging skills and dependency management in Python projects.

---

# 🚀 Future Improvements

Possible extensions include:

- Support TXT resumes
- Parse resumes directly from uploaded files
- Export results to CSV or Excel
- Build a Streamlit web interface
- Batch process hundreds of resumes
- Store results in a database
- Integrate Retrieval-Augmented Generation (RAG)
- Add semantic skill matching using embeddings

---

# 🎤 Interview Questions

### Why use Pydantic?

To validate AI-generated JSON and ensure every response follows a predefined schema.

---

### Why use JSON Mode?

To force the LLM to return valid structured data instead of unpredictable natural language.

---

### Why Temperature = 0?

Resume evaluation should be deterministic and consistent rather than creative.

---

### Why parse PDF and DOCX separately?

Different file formats require different parsing libraries before sending the text to the LLM.

---

### Why compare structured objects instead of raw text?

Structured data is easier to validate, debug, reuse, and integrate into larger AI systems.

---

# 🔑 Key Takeaway

This project demonstrates a complete AI engineering workflow—from reading real-world documents to extracting structured data, evaluating candidates with an LLM, and ranking applicants automatically.

It combines document processing, prompt engineering, structured outputs, and business logic into a practical end-to-end application that reflects the foundation of many modern AI-powered recruitment systems.

---

## 👨‍💻 Author

**Mayank**

This project is part of my **AI Engineering Roadmap**, where I document my journey of learning AI Engineering through practical implementations, mini-projects, and real-world workflows. Each milestone focuses on understanding core concepts by building applications that demonstrate how modern AI systems are designed, structured, and integrated into production-oriented pipelines.