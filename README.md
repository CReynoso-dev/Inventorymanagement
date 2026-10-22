# Inventory Management

A backend-focused inventory management application designed to help small businesses track inventory, customers, and sales while remaining simple enough for users with limited technical experience.

The project is being developed as a REST API using Python, FastAPI, SQLAlchemy, Pydantic, and SQLite. A PySide6 desktop interface is also included as an unfinished client-side prototype and may later be connected to the API.

> **Project Status:** Active Development  
> Product and customer CRUD operations are implemented across the SQLAlchemy repository, service, and FastAPI layers. Pydantic request and response models are integrated. Existing automated tests require refactoring following changes to the implementation. Database session management, transaction handling, validation, and API error handling are still being improved.

---

## Project Goals

Many inventory systems provide extensive functionality but can be difficult to configure or operate for smaller businesses.

This project aims to provide:

- Simple inventory tracking
- Sales tracking
- Customer management
- Low-friction setup
- An interface that is approachable for users with limited technical experience
- A backend architecture that can support multiple client applications

The long-term goal is to separate the backend from the user interface so that inventory operations can be accessed through a REST API.

---

## Current Features

### Database Models

The application currently uses SQLAlchemy ORM models for managing core business entities, including:

- Products
- Customers
- Sales
- Relationships between customers and their sales

UUIDs are used as primary identifiers for database records. The customer-to-sales relationship is defined in the ORM and backed by a foreign key.

Sales processing, sale line items, and inventory updates through sales are still planned.

### Repository Layer

Database operations are separated into a repository layer responsible for interacting with SQLAlchemy.

Current repository functionality includes:

- Adding products
- Adding customers
- Searching for products
- Searching for customers
- Editing product information
- Editing customer information
- Deleting products
- Deleting customers

Basic product and customer CRUD operations are implemented. Name searches use prefix matching and return matching records, while edits and deletions identify records by UUID.

The repository currently manages its own database sessions and commits. Refactoring session ownership and transaction boundaries is a planned improvement.

### Service Layer

The service layer sits between the application interface and repository layer.

Current service functionality includes:

- Product and customer creation, lookup, editing, and deletion through the repository
- Basic input type checks for creation, lookup, and deletion methods
- Conversion of string identifiers to UUIDs for edits and deletions
- Building partial updates from edit fields whose values are not `None`
- Passing repository results to the API layer

Database and repository instances are passed through constructors using dependency injection.

Validation and error handling are still being refined. Future work includes coordinating transactions at the service level or through a dedicated transaction-management abstraction.

### Automated Tests

**Status: Existing Tests Require Refactoring**

The repository contains pytest tests for the repository and service layers. However, these tests are currently broken following changes to how repository methods return data and how the application handles database operations.

The existing tests will need to be revised to match the updated implementation.

Planned testing work includes:

- Rework repository CRUD tests
- Rework service CRUD tests
- Ensure tests are independent and do not rely on execution order
- Add failure-case and edge-case tests
- Improve test database isolation and cleanup
- Add FastAPI endpoint integration tests

**Automated test coverage is not currently verified.**

### FastAPI REST API

**Status: Basic CRUD Endpoints Implemented / In Progress**

FastAPI is now integrated with the existing service and repository layers.

Current API functionality includes:

- Creating products
- Creating customers
- Searching for products by name
- Searching for customers by name
- Updating product information
- Updating customer information
- Deleting products
- Deleting customers

The API uses dependency injection to provide database, repository, and service objects to endpoint functions.

Pydantic models are implemented for validating request data and defining response structures.

Separate request models exist for creating and updating products and customers. Response models are implemented for product and customer search operations.

**Current limitations:**

- Session lifecycle management requires refactoring
- Transaction handling needs improvement
- Error responses are not yet consistently implemented
- Update operations require further validation and refinement
- Create endpoints currently return Boolean success values rather than created resource representations
- Dedicated record retrieval by UUID is not yet implemented
- API integration tests are not yet implemented

Planned API functionality includes:

- Improved REST response structures and HTTP status handling
- Product and customer retrieval by UUID
- Sales creation and retrieval
- Inventory quantity updates
- Improved validation and exception handling

The API is intended to allow different clients to communicate with the same backend without depending directly on the database implementation.

### PySide6 Client

**Status: Unfinished Client-Side Prototype**

The repository contains an earlier PySide6 graphical interface developed before the project transitioned toward an API-based architecture.

The GUI may eventually be refactored into a client application that communicates with the FastAPI backend rather than directly accessing application services.

### Barcode Scanner Support

The project also contains early barcode-scanner functionality intended to support faster product lookup and inventory operations.

---

## Architecture

The application follows a layered architecture separating HTTP handling, application logic, database operations, and persistence.

```text
Client
   |
   v
FastAPI
   |
   v
Pydantic Request Validation
   |
   v
Service Layer
   |
   v
Repository Layer
   |
   v
SQLAlchemy ORM
   |
   v
SQLite Database
```

Each layer has a separate responsibility:

**API Layer — Implemented / In Progress**  
Receives HTTP requests, uses Pydantic request and response models, calls service methods, and returns HTTP responses.

**Service Layer**  
Handles application logic, validation, and business rules.

**Repository Layer**  
Handles database queries and persistence operations using SQLAlchemy.

**Database Layer**  
Defines SQLAlchemy models, relationships, sessions, and database configuration.

**Planned Transaction Management**

The next architectural improvement focuses on establishing clear session ownership and transaction boundaries.

The intended design will allow multiple repository operations to participate in a shared transaction, with commits and rollbacks coordinated outside individual repository methods.

This will help maintain data consistency when implementing multi-step operations such as processing sales and updating inventory.

---

## Technology Stack

- **Python** — Primary programming language
- **FastAPI** — REST API and dependency injection
- **SQLAlchemy** — ORM and database interaction
- **SQLite** — Current development database
- **Pydantic** — API request validation and response models
- **pytest** — Testing framework; existing tests require refactoring
- **PySide6** — Desktop client prototype
- **UUID** — Record identifiers
- **Git / GitHub** — Version control

---

## Project Structure

```text
Inventorymanagement/
|
|-- SRC/
|   |-- API/
|   |   |-- API_TEST.py
|   |   |-- main.py
|   |   |-- request_models.py
|   |   |-- response_models.py
|   |
|   |-- Database/
|   |   |-- database.py
|   |
|   |-- Repo/
|   |   |-- Repository.py
|   |
|   |-- Service/
|       |-- Service.py
|
|-- GUI/
|   |-- Unfinished PySide6 client prototype
|
|-- Scanner/
|   |-- Early barcode scanner functionality
|
|-- Test/
|   |-- Test_SRC/
|       |-- Test_database/
|       |-- Test_repo/
|       |-- Test_service/
|
|-- README.md
```

The project structure continues to evolve as transaction management, API functionality, and automated testing are improved.

---

## Development Roadmap

Planned development includes:

- [x] Initial inventory database functionality
- [x] Repository and service layer separation
- [x] SQLAlchemy ORM integration
- [x] UUID-based database identifiers
- [x] Initial model relationships
- [x] Implement basic product and customer repository CRUD operations
- [x] Refactor the product and customer service layer to use the repository
- [x] Add Pydantic request and response models
- [x] Build initial FastAPI CRUD endpoints
- [x] Connect FastAPI endpoints to the service layer
- [x] Implement basic FastAPI dependency injection
- [ ] Refine database session lifecycle and ownership
- [ ] Implement coordinated transaction management
- [ ] Remove transaction commits from individual repository operations
- [ ] Improve error handling and validation
- [ ] Add meaningful business exceptions and HTTP error responses
- [ ] Refine partial-update behavior
- [ ] Improve API response structures and HTTP status codes
- [ ] Add dedicated UUID-based retrieval endpoints
- [ ] Refactor and repair repository and service CRUD tests
- [ ] Add failure-case and edge-case tests
- [ ] Improve test isolation, cleanup, and default test discovery
- [ ] Add FastAPI integration tests
- [ ] Implement sales and sale-line-item functionality
- [ ] Add inventory quantity updates through sales
- [ ] Improve barcode scanner integration
- [ ] Connect a client application to the REST API
- [ ] Add authentication and authorization
- [ ] Migrate from SQLite to PostgreSQL
- [ ] Containerize the application with Docker
- [ ] Deploy the backend to a cloud environment
- [ ] Explore simple product importing from structured files such as spreadsheets

---

## What I'm Learning

This project began as a smaller Python desktop application and is being progressively redesigned into a backend application with clearer separation of responsibilities.

Through the project, I am developing practical experience with:

- REST API design
- FastAPI
- Pydantic request and response models
- SQLAlchemy ORM
- Relational database design
- Primary and foreign keys
- One-to-many relationships
- Repository and service patterns
- Dependency injection
- Separation of concerns
- CRUD operations
- Data validation
- UUID identifiers
- Database sessions and transactions
- Application architecture
- Refactoring an existing codebase
- Git-based iterative development
- Automated testing with pytest and assertions

One of the main goals of the project is not only to build working functionality, but to continually improve the architecture as I learn more about backend software engineering.

---

## Current Development Focus

The SQLAlchemy models, basic product and customer repository operations, service methods, Pydantic models, and initial FastAPI CRUD endpoints are implemented.

The current focus is improving database session management and transaction boundaries before expanding the application's functionality. Existing automated tests also need to be refactored to match the updated implementation.

The development sequence is:

```text
SQLAlchemy Models — Implemented
        |
        v
Product and Customer Repository CRUD — Implemented
        |
        v
Product and Customer Service Layer — Implemented
        |
        v
Pydantic Request and Response Models — Implemented
        |
        v
FastAPI CRUD Endpoints — Implemented
        |
        v
Session Lifecycle Management — Next
        |
        v
Transaction Coordination — Planned
        |
        v
Error Handling and Validation — Planned
        |
        v
Automated CRUD Tests — Require Refactoring
        |
        v
Expanded Testing and Sales Functionality — Planned
```

The immediate objective is to establish reliable session and transaction management so that future multi-step operations can maintain database consistency, then restore and expand automated test coverage.

---

## Future Direction

The long-term goal is to make the backend independent from any individual user interface.

This would allow clients such as:

- Desktop applications
- Web applications
- Mobile applications
- Barcode-scanning interfaces

to interact with the same inventory system through an HTTP API.

Additional future functionality may include reporting, inventory alerts, sales analytics, easier data importing, PostgreSQL support, Docker deployment, and cloud hosting.

---

## Author

**Christian Reynoso**  
Computer Science Student | Backend Development | Python

GitHub: **CReynoso-dev**