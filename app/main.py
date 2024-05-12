from typing import List
from fastapi import FastAPI, HTTPException

from app.models.sessions import Session
from app.models.summaries import Summary
from database.handlers import get_session_from_db, get_summaries_from_db
from services.validator import generate_summaries

app = FastAPI(
    title="Personality Assessment API",
    description="API for managing personality assessments",
    version="1.0.0",
)


@app.get("/sessions/{session_id}", response_model=Session)
def get_session(session_id: str):
    session = get_session_from_db(session_id)
    if session:
        return Session(**session)
    else:
        raise HTTPException(status_code=404, detail="Session not found")


@app.get("/sessions/{session_id}/summaries", response_model=List[Summary])
def get_summaries(session_id: str):
    session = get_session_from_db(session_id)
    if session:
        summaries = get_summaries_from_db(session_id)
        if not summaries:
            summaries = generate_summaries(session_id)
        return [Summary(**summary) for summary in summaries]
    else:
        raise HTTPException(status_code=404, detail="Session not found")
