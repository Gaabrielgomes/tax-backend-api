# Client Management API

A simple REST API built with FastAPI for client registration and CNPJ
validation.

This project demonstrates:

-   Modular architecture
-   Separation of concerns
-   Input validation using Pydantic
-   Database persistence with SQLAlchemy
-   Unique constraint enforcement at database level

------------------------------------------------------------------------

## Tech Stack

-   FastAPI
-   SQLAlchemy 2.x
-   Pydantic v2
-   SQLite (default)

------------------------------------------------------------------------

## Project Structure

project/ │ ├── app/ │ ├── main.py │ ├── database.py │ │ │ ├── models/ │
├── schemas/ │ ├── crud/ │ └── routes/ │ └── requirements.txt

Architecture follows a layered design:

-   models → database representation
-   schemas → input/output validation
-   crud → business logic
-   routes → HTTP layer

------------------------------------------------------------------------

## Installation

Clone the repository:

git clone `<your-repository-url>`{=html} cd project

Install dependencies:

pip install -r requirements.txt

------------------------------------------------------------------------

## Running the Application

Start the development server:

uvicorn app.main:app --reload

Access the API documentation:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Endpoint

### Create Client

POST `/clients/`

Example body:

{ "name": "Empresa Teste", "cnpj": "12345678000199" }

### Validation Rules

-   CNPJ must contain only digits
-   CNPJ must contain exactly 14 digits
-   CNPJ must be unique in the database

If a duplicate CNPJ is provided, the API returns:

400 - Client with this CNPJ already exists

------------------------------------------------------------------------

## Database

By default, the project uses SQLite:

sqlite:///./database.db

The table structure:

-   id (integer, primary key)
-   name (string)
-   cnpj (string, unique, indexed)

------------------------------------------------------------------------

## Future Improvements

-   Alembic migrations
-   Unit and integration tests
-   Docker containerization
-   PostgreSQL support
-   CNPJ checksum validation
-   Authentication layer

------------------------------------------------------------------------

## Purpose of This Project

This project was built to practice:

-   Clean backend architecture
-   Proper responsibility separation
-   Data integrity enforcement
-   Professional API structure

------------------------------------------------------------------------

## Author

Gabriel Gomes
