# Poll with FastAPI

Welcome to the Poll with FastAPI project! This project demonstrates a full-stack implementation of a Poll API using FastAPI, JWT, and PostgreSQL, with automated CI/CD through GitHub Actions and containerization with Docker. It includes user authentication, data management, automated testing, and deployment.


## Project Overview
This FastAPI project allows you to:
- Greet users with a welcome message.
- Create and fetch user data.
- Create polls with various attributes.

## Technology Stack
- Framework: FastAPI
- Authentication: JWT (JSON Web Tokens)
- Database: PostgreSQL with SQLAlchemy ORM
- Containerization: Docker
- CI/CD: GitHub Actions
- Testing: Postman for manual testing, automated test scripts for continuous testing

### Prerequisites
To run this project, ensure you have:
- Python 3.6 or later.
- Poetry for dependency management. 

### How to Use
Authentication: To access the Poll API, users must authenticate with JWT. Obtain a token by providing valid credentials.
Accessing Protected Endpoints: Include the JWT token in the Authorization header to access protected endpoints.
Creating Polls: Use the POST /polls/ endpoint to create new polls. Provide the necessary data as JSON.
Fetching Polls: Access public or user-specific polls using the appropriate endpoints.

### Setup Instructions
1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv  # Create a virtual environment
   source venv/bin/activate  # Activate the virtual environment
2. Install Dependencies:
   ```bash
   poetry env use python  # Create a Poetry virtual environment with the specified Python version
3. Install all dependencies defined in pyproject.toml
   ```bash
   poetry install  # Install all dependencies defined in pyproject.toml
4. Start the server with hot reloading
   ```bash
   poetry run uvicorn main:app --reload
