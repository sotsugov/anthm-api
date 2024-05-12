def test_get_summaries_valid(client):
    response = client.get("/sessions/valid_session_id/summaries")
    assert response.status_code == 200
    assert response.json() == [
        {
            "sessionId": "valid_session_id",
            "category": "Work",
            "content": "The candidate has a strong work ethic.",
            "evaluation": [
                {
                    "sentence": "The candidate has a strong work ethic.",
                    "isInferable": True,
                    "explanation": "Supported by evidence from the interview.",
                }
            ],
        }
    ]


def test_get_summaries_invalid(client):
    response = client.get("/sessions/invalid_session_id/summaries")
    assert response.status_code == 404
    assert response.json() == {"detail": "Session not found"}
