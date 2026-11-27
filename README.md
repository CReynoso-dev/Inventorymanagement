# Inventory Management

A backend-focused inventory management application designed to help small businesses track inventory, customers, and sales while remaining simple enough for users with limited technical experience.

The project is being developed as a REST API using Python 3.14, FastAPI, SQLAlchemy, Pydantic, and SQLite. A PySide6 desktop interface is also included as an unfinished client-side prototype and may later be connected to the API.

> **Project Status:** Active Development  
> On the [`refactor/transaction-management` branch](https://github.com/CReynoso-dev/Inventorymanagement/tree/refactor/transaction-management), all eight product and customer CRUD endpoints passed live checks on Python 3.14.10. The service now uses a transaction manager, validates inputs with Pydantic, and returns records with their generated IDs. The repository and service tests still need to be updated.

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

Each repository method receives a SQLAlchemy session from the service. Inserts call `flush()` so the generated UUID is available before commit. Edits and deletions use SQL `RETURNING` to retrieve the affected record. The transaction manager owns the commit, rollback, and session cleanup.

### Service Layer

The service layer sits between the application interface and repository layer.

Current service functionality includes:

- Product and customer creation, lookup, editing, and deletion through the repository
- Validating product and customer creation and edits with shared Pydantic models
- Validating edit and delete identifiers as UUIDv4
- Applying only non-null edit fields, including valid values such as `quantity=0`
- Converting database results into `ProductDTO` and `CustomerDTO` objects while the session is open

The repository and transaction manager are passed to the service through its constructor. Each service operation opens a transaction and passes its session to the repository.

### Automated Tests

**Status: Existing Tests Require Refactoring**

The repository contains pytest tests for the database, repository, and service layers. On Python 3.14.10, collection stops in `Test_repository.py` and `Test_service.py`. Both still construct `Service(repo)`, which now also requires a transaction manager. Several tests also use older repository signatures or index returned records by position.

The test filenames start with `Test_`. From the repository root, run:

```bash
python -m pip install pytest
python -m pytest -o "python_files=Test_*.py" Test
```

With `--continue-on-collection-errors`, pytest reports **1 passed and 2 collection errors**. Separate live HTTP checks passed for all eight endpoints on the same Python version.

Planned testing work includes:

- Rework repository CRUD tests
- Rework service CRUD tests
- Ensure tests are independent and do not rely on execution order
- Add failure-case and edge-case tests
- Improve test database isolation and cleanup
- Add FastAPI endpoint integration tests

Test coverage has yet to be measured.

### FastAPI REST API

**Status: Product and Customer CRUD Implemented**

FastAPI is integrated with the existing service and repository layers. The routes in `SRC/API/API_TEST.py` expose the following operations.

| Operation | Products | Customers | Successful response |
| --- | --- | --- | --- |
| Create | `POST /item/create` | `POST /customer/create` | Created record with its UUID |
| Search by name prefix | `GET /item/{item_name}` | `GET /customer/{customer_name}` | List of matching records |
| Edit by UUID | `PUT /item/{product_id}/edit` | `PUT /customer/{customer_id}/edit` | Updated record |
| Delete by UUID | `DELETE /item/{product_id}/delete` | `DELETE /customer/{customer_id}/delete` | One-element list containing the deleted record |

Separate Pydantic models validate creates and partial updates. A product UPC must be a string of exactly 12 ASCII digits, so `"012345678905"` retains its leading zero. Quantity and price accept integers from 0 through 10,000. Customer models validate email addresses and US phone numbers. Search routes use dedicated response models.

All eight routes return `200` on success. A name search with no matches or an edit or delete for an unknown UUID returns `404`. An invalid UUID, an invalid field, or an edit containing only omitted or null fields returns `422`.

**Run the API locally**

Check out `refactor/transaction-management`. From the repository root, create a virtual environment with `python3.14 -m venv .venv` (macOS or Linux) or `py -3.14 -m venv .venv` (Windows). Activate it, then run:

```bash
python -m pip install fastapi uvicorn "SQLAlchemy>=2,<3" "pydantic[email]>=2,<3" pydantic-extra-types phonenumbers
python -c "from SRC.API.API_TEST import get_db; get_db().Create_Tables()"
python -m uvicorn SRC.API.API_TEST:app --reload
```

The initialization command creates the tables in `SRC/Database/store.db`. Open [Swagger UI](http://127.0.0.1:8000/docs) to try the routes.

**Planned API work**

- Add dedicated product and customer retrieval by UUID.
- Refine response models and HTTP status codes for writes.
- Add sales creation and retrieval, including automatic stock adjustments when a sale is recorded.
- Add endpoint integration tests to the repository.

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

**API Layer**  
Receives HTTP requests, uses Pydantic request and response models, calls service methods, and returns HTTP responses.

**Service Layer**  
Handles application logic, validation, and business rules.

**Repository Layer**  
Handles database queries and persistence operations using SQLAlchemy.

**Database Layer**  
Defines SQLAlchemy models, relationships, sessions, and database configuration.

**Transaction Management**

`Transaction_manager.start_transaction()` obtains a fresh session from the database’s `sessionmaker`. It commits when the service operation succeeds, rolls back and re-raises the exception when it fails, and always closes the session. A future sale can use this boundary to record line items and adjust stock together.

---

## Technology Stack

- **Python 3.14** — Primary programming language
- **FastAPI** — REST API and dependency injection
- **SQLAlchemy** — ORM and database interaction
- **SQLite** — Current development database
- **Pydantic v2** — Request validation, response models, and data transfer objects
- **pytest** — Automated database, repository, and service tests
- **PySide6** — Desktop client prototype
- **UUIDv4** — Record identifiers
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
|   |
|   |-- Custom_Exceptions/
|   |   |-- Custom_Error.py
|   |   |-- Exception_handler.py
|   |
|   |-- Database/
|   |   |-- database.py
|   |
|   |-- Repo/
|   |   |-- Repository.py
|   |
|   |-- Schema/
|   |   |-- DTO_models/dto_models.py
|   |   |-- request_models/request_models.py
|   |   |-- response_models/response_models.py
|   |
|   |-- Service/
|   |   |-- Service.py
|   |
|   |-- Transaction_manager/
|       |-- Transaction_manager.py
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
- [x] Refine database session lifecycle and ownership
- [x] Implement coordinated transaction management
- [x] Remove transaction commits from individual repository operations
- [x] Validate UUIDv4 identifiers, 12-digit UPCs, customer contact details, and numeric ranges
- [x] Return product and customer DTOs from service operations
- [x] Add meaningful business exceptions and HTTP error responses
- [x] Refine partial-update behavior
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

Session ownership, transaction boundaries, and partial updates are implemented. The next step is to bring the automated tests in line with the repository’s session argument, the service’s transaction-manager dependency, and the DTOs returned by service methods.

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
Session Lifecycle Management — Implemented
        |
        v
Transaction Coordination — Implemented
        |
        v
Product and Customer Error Handling and Validation — Implemented
        |
        v
Automated CRUD Tests — Require Refactoring
        |
        v
Expanded Testing and Sales Functionality — Planned
```

The immediate objective is to cover the behavior the API now supports, including zero-stock updates, invalid UPCs, missing UUIDs, and rollback when a write fails.

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