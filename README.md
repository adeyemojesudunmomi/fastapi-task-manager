FastAPI Task Manager

A production-ready REST API built with FastAPI, SQLAlchemy, and SQLite for managing tasks.

Features

- Create tasks
- Retrieve all tasks
- Retrieve a single task
- Mark tasks as completed
- Delete tasks

Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

Installation

pip install -r requirements.txt

Run

uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

to access the interactive API documentation.

API Endpoints

Method| Endpoint
GET| /
POST| /tasks
GET| /tasks
GET| /tasks/{task_id}
PUT| /tasks/{task_id}
DELETE| /tasks/{task_id}

Skills Demonstrated

- Backend Development
- REST APIs
- Database Design
- CRUD Operations
- Python Programming
- Software Engineering Fundamentals