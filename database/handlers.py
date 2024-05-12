# Mocked database functions
def get_session_from_db(session_id: str):
    # Mocked function to retrieve a session from the database
    # Replace with an actual database call
    if session_id == "valid_session_id":
        return {
            "_id": "valid_session_id",
            "customerId": "customer_id",
            "assessorId": "assessor_id",
            "startTime": "2023-05-12T10:00:00",
            "endTime": "2023-05-12T11:00:00",
            "selectedCategories": ["Work", "Relationships"],
            "status": "completed",
        }
    else:
        return None


def get_summaries_from_db(session_id: str):
    # Mocked function to retrieve summaries for a session from the database
    # Replace with an actual database call
    if session_id == "valid_session_id":
        return [
            {
                "_id": "summary_1",
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
    else:
        return []
