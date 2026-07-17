"""
Pydantic Schemas

This file contains all the data models used in the
Resume Screening application.

These schemas define the structure of data that
the LLM should return.
"""

from pydantic import BaseModel


# --------------------------------------------------------
# Resume Information
# --------------------------------------------------------

class Resume(BaseModel):
    name: str
    email: str
    phone: str
    education: str
    skills: list[str]
    experience: str
    projects: list[str]


# --------------------------------------------------------
# Job Description Information
# --------------------------------------------------------

class JobDescription(BaseModel):
    job_title: str
    required_skills: list[str]
    preferred_skills: list[str]
    minimum_experience: str
    education: str


# --------------------------------------------------------
# Final Matching Result
# --------------------------------------------------------

class MatchResult(BaseModel):
    candidate_name: str
    match_percentage: int
    matched_skills: list[str]
    missing_skills: list[str]
    recommendation: str