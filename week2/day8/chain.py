import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"


JD="""
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience
"""
RESUME="""
Name: Rahul Sharma

Experience:
3 years as a Software Developer.

Skills:
Python, FastAPI, Django, MySQL, Docker,
REST APIs, Git

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""

def ask_llm(system_prompt, user_prompt):
    sys_msg={
        "role": "system",
        "content": system_prompt
    }
    user_msg={
        "role": "user",
        "content": user_prompt
    }
    messages=[sys_msg, user_msg]
    resposne=client.chat.completions.create(model=model, messages=messages,temperature = 0)
    answer=resposne.choices[0].message.content
    return answer


def step1_res_extract(RESUME):
    print("STEP 1")
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the candidates resume provided.
    Only return the skills no other information. Do not invent any skillsby yourself.
    Output Format:
    Skills should be separated by commas. Just return comma separated skills do not return any other filler information
    """
    user_prompt=f"""
    Extract the skills from this resume
    {RESUME}
    """
    return ask_llm(system_prompt, user_prompt)

def step2_JD_extract(JD):
    print("step2")
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the Job description  provided.
    Only return the skills no other information. Do not invent any skills by yourself.
    Output Format:
    Skills should be separated by commas. Just return comma separated skills do not return any other filler information
    """
    user_prompt=f"""
    Extract the skills from this JD
    {JD}
    """
    return ask_llm(system_prompt, user_prompt)

def step3_match(candidate,jd):
    print("step3")
    system_prompt="""
    You are a professional HR assistant. compare the skills of candidate and the skills required in the JD and produce a final score between
    1 and 100. also produce a short verdict whther the candidate is a good fit for the role.
    """
    user_prompt=f"""
    Compare and matc h the skills
    JD:
    {jd}
    Candidate:
    {candidate}
    """
    return ask_llm(system_prompt, user_prompt)

candidate=step1_res_extract(RESUME)
print(candidate)
sleep(2)
jd=step2_JD_extract(JD)
print(jd)
sleep(2)
score=step3_match(candidate,jd)
print(score)


"""
TERMINAL OUTPUT:
(day8) PS D:\CUDA projects\Practice\AI Engineer Roadmap\week2\day8> python .\chain.py
STEP 1
Python, FastAPI, Django, MySQL, Docker, REST APIs, Git
step2
Python, FastAPI, Django, PostgreSQL, Docker, AWS, REST APIs
step3
To compare and match the skills, I'll break down the required skills in the Job Description (JD) and the skills possessed by the candidate.

**Required Skills in JD:**

1. Python
2. FastAPI
3. Django
4. PostgreSQL
5. Docker
6. AWS
7. REST APIs

**Candidate's Skills:**

1. Python
2. FastAPI
3. Django
4. MySQL
5. Docker
6. REST APIs
7. Git

**Matching Skills:**

1. Python (Match)
2. FastAPI (Match)
3. Django (Match)
4. Docker (Match)
5. REST APIs (Match)

**Non-Matching Skills:**

1. PostgreSQL (Required) vs. MySQL (Candidate) - Similar skill, but not exact match
2. AWS (Required) - Not present in Candidate's skills
3. Git (Candidate) - Not required in JD, but a valuable additional skill

**Score Calculation:**

Out of the 7 required skills, the candidate matches 5 skills exactly. For the 2 non-matching skills, I'll assign a partial score:

* PostgreSQL vs. MySQL: 0.5 (similar skill, but not exact match)
* AWS: 0 (not present in Candidate's skills)

Total Score: (5 x 1) + 0.5 + 0 = 5.5 / 7 = 78.57%

Rounded Score: 79

**Verdict:**
The candidate is a good fit for the role, but may require some training or adaptation to work with PostgreSQL and AWS. Overall, they possess a strong foundation in Python, FastAPI, Django, and Docker, which are crucial skills for the position. With some additional learning, they can become a valuable asset to the team.
"""