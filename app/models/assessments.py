from pydantic import BaseModel
from typing import List


class AssessmentEvaluation(BaseModel):
    inferabilityScore1: float
    inferabilityScore2: float


class AssessmentQuestion(BaseModel):
    question: str
    answer: str
    evidence: List[str]
    evaluation: AssessmentEvaluation


class AssessmentPart(BaseModel):
    partId: str
    questions: List[AssessmentQuestion]


class Assessment(BaseModel):
    _id: str
    sessionId: str
    category: str
    parts: List[AssessmentPart]
