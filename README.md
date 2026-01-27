# SkillSwap Hub

## Overview

SkillSwap Hub is a Django-based full-stack web application for listing skills and creating exchange requests between users. It provides authentication, CRUD features, and a clean, accessible UI.

## Features

- User registration, login, and logout
- Skill listing and detail views
- Create, update, and delete skills
- Submit and track exchange requests
- Role-based access controls for protected actions
- Responsive, accessible UI with clear validation and feedback

## Tech Stack

- Django
- SQLite (development)
- HTML/CSS

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Apply migrations:
   - `python manage.py migrate`
4. Run the server:
   - `python manage.py runserver`

## Environment Variables

Store secrets in environment variables and keep them out of version control. Typical variables:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`

## Testing

Run the test suite:

- `pytest`

## Accessibility

- HTML templates include clear labels, error messages, and feedback.
- Navigation and forms are designed to be keyboard-friendly.
- Contrast and layout are optimized for readability.

## Deployment

- The project includes `Procfile` and `runtime.txt` for platform deployments.
- Configure production settings for security (e.g., `DEBUG=False`, secure cookies, allowed hosts).
- Use environment variables for secrets and database configuration.

## Security

- Do not commit secrets.
- Use Django’s built-in authentication and CSRF protection.
- Ensure database and credentials are not stored in the repository.

## Database Schema (ERD)

```mermaid
erDiagram
    User ||--o{ Skill : owns
    User ||--o{ ExchangeRequest : creates
    Category ||--o{ Skill : categorizes
    Skill ||--o{ ExchangeRequest : receives
    
    User {
        int id PK
        string username
        string email
        string password
        datetime date_joined
    }
    
    Category {
        int id PK
        string name
        string slug
    }
    
    Skill {
        int id PK
        int owner_id FK
        int category_id FK
        string title
        text description
        datetime created_at
    }
    
    ExchangeRequest {
        int id PK
        int skill_id FK
        int requester_id FK
        string status
        datetime created_at
    }
```

The database consists of four main models:

- **User** (Django's built-in auth model): Manages user authentication and profiles
- **Category**: Organizes skills into categories with URL-friendly slugs
- **Skill**: Core entity representing skills users can offer, owned by users and optionally categorized
- **ExchangeRequest**: Tracks requests between users for skill exchanges with status (pending, accepted, rejected, cancelled)

Key relationships:
- Users can own multiple skills and create multiple exchange requests
- Skills belong to one user and optionally one category
- Exchange requests link a requester (User) to a specific skill
- Categories can contain multiple skills

## Project Structure

- `accounts/` user auth and profiles
- `skills/` skill listings and CRUD
- `exchanges/` exchange requests and workflow
- `core/` project configuration
- `templates/` HTML templates
- `tests/` automated tests

## AI Tooling (Reflection)

This project may use AI assistance to:

- Draft documentation and test outlines
- Summarize accessibility checks
- Suggest refactoring or linting improvements
