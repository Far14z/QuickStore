# QuickStore API Application

## Summary

QuickStore is a fictional e-commerce REST API built with FastAPI, SQLAlchemy and MySQL, designed as a practical implementation of **Clean Architecture**. This project serves as an eduactional resource
for understanding how to structure modern Python applications to serve as a reference for future projects.

## Features
- **RESTful Api** with HTTP semantics and status codes
- **OpenApi Documentation** automatically generated from code
- **Swagger UI** for API exploration and testing
- **FastApi Framework** leveraging modern Python features
- **SQLAlchemy ORM** with repository pattern implementation
- **Clean Architecture** with clear layer separation
- **Alembic** for database migrations
- **Python dotenv** for environment variables management

## Configuration

- Add requirements.txt: 
    - `pip freeze > requirements.txt`


- Add the SQLAlchemy dependency and MySQl driver:
    - dependency: `pip install SQLAlchemy`
    - driver: `pip install mysql-connector-python`


- Add the Alembic dependency: 
    - `pip install alembic`


- Add the Python dotenv dependency:
    - `pip install python-dotenv`

## Clean Architecture Layers

In this project, we have implemented the following layers of Clean Architecture:

- **Application**:
- **Domain**: 
- **Infrastructure**
- **Presentation**


