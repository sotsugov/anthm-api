# Mocked AI service functions
def generate_summaries(session_id: str):
    # Mocked function to generate summaries using an AI service
    # Replace with actual AI service call
    return [
        {
            "_id": "summary_1",
            "sessionId": session_id,
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
