# QuickStore API Application

## Summary

QuickStore is a fictional e-commerce REST API built with FastAPI, SQLAlchemy and MySQL, designed as a practical implementation of **Clean Architecture** with CQRS Pattern. This project serves as an eduactional resource
for understanding how to structure modern Python applications to serve as a reference for future projects.

## Features
- **RESTful Api** with HTTP semantics and status codes
- **OpenApi Documentation** automatically generated from code
- **Swagger UI** for API exploration and testing
- **FastApi Framework** leveraging modern Python features
- **SQLAlchemy ORM** with repository pattern implementation
- **Clean Architecture** with clear layer separation
- **Python dotenv** for environment variables management
- **BCrypt** for password hashing

## Configuration

- Use this command to get the requirements.txt: 
    - `pip freeze > requirements.txt`


- Add the SQLAlchemy dependency and AioMySql driver:
    - dependency: `pip install SQLAlchemy`
    - driver: `pip install aiomysql`


- Add the ByCrypt dependency:
    - `pip install bcrypt` 


- Add the Python dotenv dependency:
    - `pip install python-dotenv`


## Dependencies

- **SQLAlchemy**: This is a Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. 


- **AioMySql**: A MySQL client for asyncio and Python.


- **BCrypt**: A library for hashing passwords securely and efficiently.


- **DotEnv**: A Python library for reading key-value pairs from a .env file.

## Clean Architecture Layers

In this project, we have implemented the following layers of Clean Architecture with a feature-based approach:

For the Users feature we have the following layers:

### **Domain**:
- Models:
    - Entities: The main class for this layer is the User entity.
    - Commands: We use the CQRS pattern to implement commands. For example, SignUpCommand
- Repositories: The UserRepository interface defines the contract for user-related data operations.
- Handlers: The UserHandlerInterface defines the contract for user-related business logic. 

### **Infrastructure**
- Persistence: The UserModel class to map the User entity to a database table.
- Repository: The UserRepository implementation uses SQLAlchemy to interact with the database.
- Mappers: The UserMapper class implements the UserMapperInterface interface.

### **Application**:
- Handlers:
    - Commands: The UserCommandHandler class implements the UserCommandHandlerInterface interface. 

### **Presentation**
- Controllers: The UserController class handles HTTP requests and responses related to users.
- Routers: The UserRouter class defines the routes for the UsersController.
- Schemas: 
    - Assemblers: Converts objects from the external system to objects in the application/domain layer 
    - Resources: Defines internal and external schemas for the API.


