def test_get_session_valid(client):
    response = client.get("/sessions/valid_session_id")
    assert response.status_code == 200
    assert response.json() == {
        "customerId": "customer_id",
        "assessorId": "assessor_id",
        "startTime": "2023-05-12T10:00:00",
        "endTime": "2023-05-12T11:00:00",
        "selectedCategories": ["Work", "Relationships"],
        "status": "completed",
    }


def test_get_session_invalid(client):
    response = client.get("/sessions/invalid_session_id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Session not found"}
