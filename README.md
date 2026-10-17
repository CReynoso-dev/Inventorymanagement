# Inventory Management

A backend-focused inventory management application designed to help small businesses track inventory, customers, and sales while remaining simple enough for users with limited technical experience.

The project is being developed as a REST API using Python, FastAPI, SQLAlchemy, and SQLite. A PySide6 desktop interface is also included as an unfinished client-side prototype and may later be connected to the API.

> **Project Status:** Active Development  
> Product and customer CRUD operations are implemented in the SQLAlchemy repository and service layers, with basic automated tests. FastAPI integration is at the initial scaffolding stage; API CRUD endpoints are not implemented yet.

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

UUIDs are used as primary identifiers for database records. The customer-to-sales relationship is defined in the ORM and backed by a foreign key. Sales processing, sale line items, and inventory updates through sales are still planned.

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

Basic product and customer CRUD operations are implemented. Name searches use prefix matching, while edits and deletions identify records by UUID. Error handling and edge cases are still being improved.

### Service Layer

The service layer sits between the application interface and repository layer.

Current service functionality includes:

- Product and customer creation, lookup, editing, and deletion through the repository
- Basic input type checks for creation, lookup, and deletion methods
- Conversion of string identifiers to UUIDs for edits and deletions
- Building partial updates from edit fields whose values are not `None`

Database and repository instances are passed through constructors using dependency injection. This keeps service logic separate from direct database access. Validation, error handling, and session lifecycle management still need further work.

### Automated Tests

The repository includes 12 basic pytest tests across the repository and service layers:

- Product and customer creation, checked through name lookups
- Product and customer editing, checked through updated names
- Product and customer deletion, checked by confirming searches return no matching records

Each CRUD test creates its own sample records. A separate database initialization smoke test is also included. The tests currently use file-backed SQLite databases. Failure-case tests and database cleanup are not implemented yet.

### FastAPI REST API

**Status: Initial Scaffolding / In Progress**

FastAPI is being introduced as the primary interface to the backend. The repository currently contains a starter FastAPI app and a placeholder route; the API is not yet connected to the service layer, and CRUD endpoints are not implemented.

Planned API functionality includes endpoints for:

- Product CRUD operations
- Customer CRUD operations
- Sales creation and retrieval
- Inventory updates
- Inventory searches

The API will allow different clients to communicate with the same backend without depending directly on the database implementation.

### PySide6 Client

**Status: Unfinished Client-Side Prototype**

The repository contains an earlier PySide6 graphical interface developed before the project transitioned toward an API-based architecture.

The GUI may eventually be refactored into a client application that communicates with the FastAPI backend rather than directly accessing application services.

### Barcode Scanner Support

The project also contains early barcode-scanner functionality intended to support faster product lookup and inventory operations.

---

## Architecture

The database, repository, and service layers are implemented. The intended full architecture adds FastAPI and client applications around those layers:

```text
Client
   │
   ▼
FastAPI
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
Database
```

Each layer has a separate responsibility:

**API Layer — Planned Integration**  
Will receive HTTP requests, call the service layer, and return responses.

**Service Layer**  
Handles application logic, validation, and business rules.

**Repository Layer**  
Handles database queries and persistence operations.

**Database Layer**  
Defines SQLAlchemy models, relationships, sessions, and database configuration.

This separation allows individual parts of the application to change without requiring the entire system to be rewritten.

---

## Technology Stack

- **Python**
- **FastAPI** — Initial API scaffolding; CRUD endpoints planned
- **SQLAlchemy** — ORM and database interaction
- **SQLite** — Current development database
- **Pydantic** — Planned API request and response models
- **pytest** — Basic repository, service, and database tests
- **PySide6** — Desktop client prototype
- **UUID** — Record identifiers
- **Git / GitHub** — Version control

---

## Project Structure

```text
Inventorymanagement/
│
├── SRC/
│   ├── API/
│   │   └── FastAPI application development
│   │
│   ├── Database/
│   │   └── SQLAlchemy models and database configuration
│   │
│   ├── Repo/
│   │   └── Database access and CRUD operations
│   │
│   └── Service/
│       └── Business logic and validation
│
├── GUI/
│   └── Unfinished PySide6 client prototype
│
├── Scanner/
│   └── Early barcode scanner functionality
│
├── Test/
│   └── Test_SRC/
│       ├── Test_database/
│       ├── Test_repo/
│       └── Test_service/
│
└── README.md
```

The structure is continuing to evolve as automated testing is expanded and FastAPI is connected to the existing backend layers.

---

## Development Roadmap

Planned development includes:

- [x] Initial inventory database functionality
- [x] Repository and service layer separation
- [x] SQLAlchemy ORM integration
- [x] UUID-based database identifiers
- [x] Initial model relationships
- [x] Implement basic product and customer repository CRUD operations
- [x] Add basic automated repository and service CRUD tests
- [x] Refactor the product and customer service layer to use the repository
- [ ] Add failure-case and edge-case tests
- [ ] Improve test isolation, cleanup, and default test discovery
- [ ] Refine database session lifecycle and transaction handling
- [ ] Add Pydantic request and response models
- [ ] Build FastAPI CRUD endpoints
- [ ] Implement sales and sale-line-item functionality
- [ ] Add inventory quantity updates through sales
- [ ] Improve barcode scanner integration
- [ ] Connect a client application to the REST API
- [ ] Improve error handling and validation
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

The SQLAlchemy models, basic product and customer repository operations, service methods, and initial CRUD tests are in place. The current focus is strengthening validation and tests before connecting the backend to FastAPI.

The development sequence is:

```text
SQLAlchemy Models — Implemented
        ↓
Product and Customer Repository CRUD — Implemented
        ↓
Product and Customer Service Layer — Implemented
        ↓
Basic Automated CRUD Tests — Added
        ↓
Failure-Case Tests and Validation — Next
        ↓
FastAPI CRUD Endpoints — Planned
```

Once the backend layers are stable, FastAPI will become the primary entry point into the application.

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