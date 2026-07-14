"""
Resume Screening Application

Version 1

This application reads a resume from a text file,
uses a Large Language Model (LLM) to extract structured
information in JSON format, validates the response using
Pydantic, and converts it into a Python object.

Author: Mayank
"""

# STEP 1: Import Required Libraries
import os
import json

from dotenv import load_dotenv
from groq import Groq
from schema import Resume, JobDescription, MatchResult


# STEP 2: Load Environment Variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please check your .env file.")



# STEP 3: Create Groq Client
client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"


# Helper Function
def extract_structured_data(text, model_class, parser_role):
    """
    Extract structured information from text using an LLM
    and validate it using a Pydantic model.
    """

    schema = model_class.model_json_schema()

    system_prompt = f"""
    You are an AI {parser_role}.

    Extract information from the given text.

    Return ONLY valid JSON.

    Follow this schema strictly.

    {schema}
    """

    messages = [

        {
            "role": "system",
            "content": system_prompt
        },

        {
            "role": "user",
            "content": text
        }

    ]

    response = client.chat.completions.create(

        model=MODEL,

        messages=messages,

        response_format={
            "type": "json_object"
        },

        temperature=0

    )

    answer = response.choices[0].message.content

    print("\n")
    print("=" * 60)
    print(f"RAW {parser_role.upper()} JSON")
    print("=" * 60)

    print(answer)

    data = json.loads(answer)

    return model_class(**data)


# STEP 4: Read Resume File
with open("data/resume.txt", "r", encoding="utf-8") as file:
    resume = file.read()



# STEP 5: Read Job Description
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()



# STEP 6: Extract Resume Information
resume_data = extract_structured_data(
    resume,
    Resume,
    "Resume Parser"
)

print("\n")
print("=" * 60)
print("PARSED RESUME")
print("=" * 60)

print(resume_data)


# STEP 7: Extract Job Description Information
job = extract_structured_data(
    job_description,
    JobDescription,
    "Job Description Parser"
)

print("\n")
print("=" * 60)
print("PARSED JOB DESCRIPTION")
print("=" * 60)

print(job)



# STEP 8: Compare Resume Skills with Job Requirements

# Convert skills to lowercase for comparison while preserving original names
resume_skill_map = {
    skill.lower(): skill
    for skill in resume_data.skills
}

required_skill_map = {
    skill.lower(): skill
    for skill in job.required_skills
}

preferred_skill_map = {
    skill.lower(): skill
    for skill in job.preferred_skills
}

resume_skills = set(resume_skill_map.keys())
required_skills = set(required_skill_map.keys())
preferred_skills = set(preferred_skill_map.keys())


matched_required = sorted(
    required_skill_map[skill]
    for skill in resume_skills & required_skills
)

missing_required = sorted(
    required_skill_map[skill]
    for skill in required_skills - resume_skills
)

matched_preferred = sorted(
    preferred_skill_map[skill]
    for skill in resume_skills & preferred_skills
)

missing_preferred = sorted(
    preferred_skill_map[skill]
    for skill in preferred_skills - resume_skills
)


# STEP 9: Calculate Match Percentage
required_score = 70
preferred_score = 30

required_percentage = (
    len(matched_required) / len(required_skills)
) * required_score

preferred_percentage = (
    len(matched_preferred) / len(preferred_skills)
) * preferred_score

match_percentage = round(required_percentage + preferred_percentage)


# STEP 10: Generate Recommendation
if match_percentage >= 80:
    recommendation = "Shortlist for Interview"

elif match_percentage >= 60:
    recommendation = "Consider for Interview"

else:
    recommendation = "Reject"



# STEP 11: Create Match Report

# Remove duplicate skills (if any) and sort alphabetically
matched_skills = sorted(
    set(matched_required + matched_preferred)
)

missing_skills = sorted(
    set(missing_required + missing_preferred)
)

result = MatchResult(

    candidate_name=resume_data.name,

    match_percentage=match_percentage,

    matched_skills=matched_skills,

    missing_skills=missing_skills,

    recommendation=recommendation

)


# STEP 12: Save JSON Report
with open(
    "outputs/screening_report.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        result.model_dump(),
        file,
        indent=4
    )



# STEP 13: Save Text Report
report = f"""
========================================
RESUME SCREENING REPORT
========================================

Candidate
{result.candidate_name}

----------------------------------------

Match Percentage
{result.match_percentage}%

----------------------------------------

Matched Skills

{chr(10).join(f"✔️ {skill}" for skill in result.matched_skills)}

----------------------------------------

Missing Skills

{chr(10).join(f"❌ {skill}" for skill in result.missing_skills)}

----------------------------------------

Recommendation

{result.recommendation}
"""

with open(
    "outputs/screening_report.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(report.strip())





# STEP 14: Display Final Report
print("\n")
print("=" * 40)
print("RESUME SCREENING REPORT")
print("=" * 40)

print(f"\nCandidate : {result.candidate_name}")

print(f"\nMatch Percentage : {result.match_percentage}%")

print("\nMatched Skills")

if result.matched_skills:
    for skill in result.matched_skills:
        print(f"✓ {skill}")
else:
    print("None")

print("\nMissing Skills")

if result.missing_skills:
    for skill in result.missing_skills:
        print(f"❌ {skill}")
else:
    print("None")

print("\nRecommendation")

print(f"✅ {result.recommendation}")

