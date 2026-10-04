# Cyber Risk Register API

## Overview

I am building a portfolio project called Cybersecurity Risk Register API to strengthen my skills for entry-level Python/backend developer jobs.
My goal is to learn by building a realistic backend application that I can eventually place on my GitHub, resume, and portfolio and discuss confidently during interviews.

```
Windows Development Machine
│
├── VS Code
├── PowerShell
├── Git
└── Docker
     │
     └── Docker Compose
          │
          ├── FastAPI container
          │
          └── PostgreSQL container
                 │
                 └── Persistent volume

                     CLIENT
        Swagger UI / curl / API client
                       │
                       │ HTTP / JSON
                       ▼
              ┌─────────────────┐
              │     FastAPI     │
              │   REST API      │
              └────────┬────────┘
                       │
              Request validation
                 Pydantic models
                       │
                       ▼
              ┌─────────────────┐
              │ Business Logic  │
              │ Risk scoring    │
              │ Severity        │
              │ CRUD operations │
              └────────┬────────┘
                       │
                 Database layer
                       │
                       ▼
              ┌─────────────────┐
              │   PostgreSQL    │
              │                 │
              │ risks           │
              │ users           │
              │ etc.            │
              └─────────────────┘
...

## Project Status
 
The project is currently in its initial development and setup phase.
