# A-m example API

FastAPI-based application that provides endpoints for managing personality assessments. It allows you to retrieve session details and generate summaries based on session data.


* The app/ directory contains the main FastAPI application code.

* The tests/ directory contains the test files for the API endpoints.

## Installation

Create and activate virtual environment
```shell
python3 -m venv .venv
source .venv/bin/activate
```

Within the environment install dependencies and
```shell
pip install -r requirements.txt
```

Start the FastAPI server:
```shell
uvicorn app.main:app --reload
```

## Testing
The API endpoints are tested using the pytest testing framework. The test files are located in the tests/ directory.

To run the tests, use the following command:
```shell
pytest tests/
```

## Preview deployment on main branch
The main branch is autmatically deployed to Vercel
