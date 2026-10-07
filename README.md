# Inventory Management System

A backend-focused inventory management application designed to help small businesses track inventory, customers, and sales while remaining simple enough for users with limited technical experience.

The project is being developed as a REST API using Python, FastAPI, SQLAlchemy, and SQLite. A PySide6 desktop interface is also included as an unfinished client-side prototype and may later be connected to the API.

> **Project Status:** Active Development  
> The SQLAlchemy data layer and repository architecture are currently being developed and refactored. FastAPI integration is in progress.

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

UUIDs are used as primary identifiers for database records.

### Repository Layer

Database operations are separated into a repository layer responsible for interacting with SQLAlchemy.

Current repository functionality includes:

- Adding products
- Adding customers
- Searching for products
- Searching for customers
- Editing product information
- Editing customer information

Additional CRUD functionality is currently being implemented.

### Service Layer

The service layer sits between the application interface and repository layer.

Its purpose is to handle:

- Business rules
- Input validation
- Coordination between repository operations
- Application-level logic

This keeps business logic separate from direct database access.

### FastAPI REST API

**Status: In Progress**

FastAPI is being integrated as the primary interface to the backend.

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

The backend is being organized using a layered architecture:

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

**API Layer**  
Receives HTTP requests and returns responses.

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
- **FastAPI** — REST API development
- **SQLAlchemy** — ORM and database interaction
- **SQLite** — Current development database
- **Pydantic** — API request and response validation
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
│   └── Barcode scanner functionality
│
└── README.md
```

The structure is continuing to evolve as the backend is refactored around FastAPI and SQLAlchemy.

---

## Development Roadmap

Planned development includes:

- [x] Initial inventory database functionality
- [x] Repository and service layer separation
- [x] SQLAlchemy ORM integration
- [x] UUID-based database identifiers
- [x] Initial model relationships
- [ ] Complete repository CRUD operations
- [ ] Add automated repository and service tests
- [ ] Complete service-layer refactor
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

One of the main goals of the project is not only to build working functionality, but to continually improve the architecture as I learn more about backend software engineering.

---

## Current Development Focus

The current development focus is completing the transition from the application's original database implementation to SQLAlchemy.

The immediate development sequence is:

```text
SQLAlchemy Models
        ↓
Repository CRUD
        ↓
Service Layer
        ↓
Automated Tests
        ↓
FastAPI Endpoints
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
