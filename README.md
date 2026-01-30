![SkillSwap Hub logo](static/brand/skillswap-logo.svg)

# SkillSwap Hub

- [Project board](https://github.com/users/cstuart756/projects/10/views/1)
- [Live site](https://skillswap-hub-cstuart756-df93470f789d.herokuapp.com/)

## Table of Contents

- [Project Board](#project-board)
- [Overview](#overview)
- [Features](#features)
- [Final Product](#final-product)
- [Wireframes](#wireframes)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [Testing](#testing)
- [Accessibility](#accessibility)
- [Deployment](#deployment)
- [Security](#security)
- [Database Schema (ERD)](#database-schema-erd)
- [User Stories (MoSCoW)](#user-stories-moscow)
- [Project Structure](#project-structure)
- [AI Tooling (Reflection)](#ai-tooling-reflection)
  - [Responsible AI Use](#responsible-ai-use)
- [Credits](#credits)

## Overview

SkillSwap Hub is a Django-based full-stack web application for listing skills and creating exchange requests between users. It provides authentication, CRUD features, and a clean, accessible UI.

#### GitHub Project Board

![GitHub Project Board](static/brand/skillswapprojectboard.png)

## Features

- User registration, login, and logout
- Skill listing and detail views
- Create, update, and delete skills
- Submit and track exchange requests
- Role-based access controls for protected actions
- Responsive, accessible UI with clear validation and feedback

## Wireframes

Below are the main UI wireframes for the SkillSwap Hub project. These illustrate the core user flows and admin features.

<details>
<summary>Desktop - Skill Listings, User Dashboard, Create/Edit Skill</summary>

![Skill Listings, User Dashboard, Create/Edit Skill](static/brand/desktopwireframe.png)

</details>

<details>
<summary>Mobile - Skill Listings, Skill Detail, Login/Register, User Dashboard, Create/Edit Skill</summary>

![Mobile Skill Listings, Detail, Login, Dashboard, Create/Edit](static/brand/mobilewireframe.png)

</details>

<details>
<summary>Mobile - Home/Skill Listings, Skill Detail, Login/Register, Dashboard, Create/Edit Skill</summary>

![Mobile Home, Detail, Login, Dashboard, Create/Edit](static/brand/mobilewireframe0.png)

</details>

<details>
<summary>Tablet Wireframe</summary>

![Tablet Wireframe](static/brand/tabletwireframe.png)

</details>

<details>
<summary>Tablet Wireframe 2</summary>

![Tablet Wireframe 2](static/brand/tabletwireframe0.png)

</details>

<details>
<summary>Mobile Wireframe</summary>

![Mobile Wireframe](static/brand/mobilewireframe.png)

</details>

<details>
<summary>Mobile Wireframe 2</summary>

![Mobile Wireframe 2](static/brand/mobilewireframe0.png)

</details>

## Final Product

<details>
<summary>Desktop</summary>

![Final product desktop view](docs/final-product-desktop.png)

</details>

<details>
<summary>Mobile</summary>

![Final product mobile view](docs/final-product-mobile.png)

</details>

<details>
<summary>Login</summary>

![Final product login](docs/final-product-login.png)

</details>

<details>
<summary>Register</summary>

![Final product register](docs/final-product-register.png)

</details>

<details>
<summary>Offer Skill</summary>

![Final product offer skill](docs/final-product-offer-skill.png)

</details>

<details>
<summary>Skill Details</summary>

![Final product skill details](docs/final-product-skill-details.png)

</details>

<details>
<summary>Exchange Dashboard</summary>

![Final product exchange dashboard](docs/final-product-exchange-dashboard.png)

</details>

<details>
<summary>Exchange Details</summary>

![Exchange Details](static/brand/exchangedetails.png)

</details>

<details>
<summary>Exchange Submitted</summary>

![Exchange Submitted](static/brand/exchangesubmitted.png)

</details>

## Tech Stack

- Python 3
- Django
- SQLite (development)
- PostgreSQL (production)
- HTML/CSS
- pytest + pytest-django
- Playwright + axe-playwright (accessibility testing)
- Gunicorn + WhiteNoise

## Setup

1. Clone the repository:
   - `git clone https://github.com/cstuart756/skillswap-hub.git`
2. Change into the project directory:
   - `cd skillswap-hub`
3. Create a virtual environment:
   - `python -m venv .venv`
4. Activate the virtual environment:
   - macOS/Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
5. Install dependencies:
   - `pip install -r requirements.txt`
6. Apply migrations:
   - `python manage.py migrate`
7. Run the server:
   - `python manage.py runserver`

## Environment Variables

Store secrets in environment variables and keep them out of version control. Typical variables:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`

## Testing

### Automated testing

Run the test suite:

- `pytest`

### Pytest Results

- Latest run (2026-01-30): 1 test passed
- Scope: [tests/test_request_flow.py](tests/test_request_flow.py)

### Manual testing

Checklist:

- ✅ Register
- ✅ Login
- ✅ Offer skill
- ✅ View skills
- ✅ Register interest in a skill
- ✅ View sent and received requests
- ✅ Accept request
- ✅ Add contact details
- ✅ Exchange contact details
- ✅ Logout
- ✅ PEP8 check (pycodestyle)

<details>
<summary>Lighthouse Desktop</summary>

![Lighthouse Desktop](static/brand/skillswaplighthousedesktop.png)

</details>

<details>
<summary>Lighthouse Mobile</summary>

![Lighthouse Mobile](static/brand/skillswaplighthousemobile.png)

</details>

## Accessibility

- HTML templates include clear labels, error messages, and feedback.
- Navigation and forms are designed to be keyboard-friendly.
- Contrast and layout are optimized for readability.

## Deployment

### Deploy to Heroku

1. Create a Heroku app:
   - `heroku create skillswap-hub`
2. Add the Postgres addon:
   - `heroku addons:create heroku-postgresql:hobby-dev`
3. Configure environment variables:
   - `heroku config:set SECRET_KEY=your-secret-key`
   - `heroku config:set DEBUG=False`
   - `heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com`
   - `heroku config:set DJANGO_CSRF_TRUSTED_ORIGINS=https://your-app-name.herokuapp.com`
4. Push to Heroku:
   - `git push heroku main`
5. Apply migrations:
   - `heroku run python manage.py migrate`
6. (Optional) Seed sample data:
   - `heroku run python manage.py seed_sample_data`
7. Collect static files (if required):
   - `heroku run python manage.py collectstatic --noinput`
8. Open the app:
   - `heroku open`

Notes:

- This project already includes a `Procfile` and `runtime.txt`.
- For production, keep `DEBUG=False` and use environment variables for secrets.

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

## User Stories (MoSCoW)

### Must Have

1. **Register an account**
   - As a new user, I want to create an account so I can list and request skills.
2. **Log in and log out**
   - As a user, I want to log in and log out so my account stays secure.
3. **Browse skills**
   - As a visitor, I want to browse available skills so I can find an exchange.
4. **View skill details**
   - As a user, I want to view a skill’s details so I can decide whether to request it.
5. **Create a skill listing**
   - As a user, I want to create a skill listing so I can offer my skills to others.
6. **Request a skill exchange**
   - As a user, I want to request a skill exchange so I can trade with another user.
7. **Manage requests**
   - As a skill owner, I want to accept or reject requests so I can control who I exchange with.

### Should Have

1. **Edit and delete skills**
   - As a user, I want to edit or remove my listings so they stay accurate.
2. **View my request dashboard**
   - As a user, I want to see sent and received requests so I can manage exchanges.
3. **Filter and sort skills**
   - As a user, I want to filter and sort skills so I can find relevant listings faster.
4. **Status feedback**
   - As a user, I want to see clear request status (pending/accepted/rejected/cancelled) so I know what’s happening.

### Could Have

1. **Categories for skills**
   - As a user, I want to categorize skills so browsing is easier.
2. **Search by keyword**
   - As a user, I want to search by keyword so I can quickly find specific skills.
3. **Accessible UI hints**
   - As a user, I want accessible feedback and tooltips so the UI is easy to understand.

### Won’t Have (for now)

1. **Real-time chat**
   - As a user, I want live chat so I can negotiate exchanges in real time.
2. **Payment handling**
   - As a user, I want to pay for premium features so I can unlock extra services.
3. **Ratings and reviews**
   - As a user, I want to rate exchanges so I can build trust in the community.

## Project Structure

- `accounts/` user auth and profiles
- `skills/` skill listings and CRUD
- `exchanges/` exchange requests and workflow
- `core/` project configuration
- `templates/` base templates and shared includes
- `static/` CSS and shared assets
- `docs/` documentation images (final product and wireframes)
- `tests/` automated tests (pytest)
- `manage.py` Django management entry point
- `requirements.txt` Python dependencies

## AI Tooling (Reflection)

AI-assisted tooling was used as a supportive development aid during the planning and implementation of this project. All final code decisions, integration, and testing were performed by the developer.

AI was used to:

- 📐 Planning & Architecture
  - Assist in breaking down user stories into technical tasks aligned with Agile methodology.
  - Suggest database relationships and model responsibilities during early ERD design.
  - Help validate Django app separation (accounts, skills, exchanges) against best-practice conventions.
- 🧠 Problem Solving & Debugging
  - Provide explanations of Django error messages and tracebacks to support debugging.
  - Suggest alternative approaches to view logic and form validation where initial implementations failed.
  - Help reason about permission handling and request lifecycle states (pending, accepted, rejected, cancelled).
- 🧪 Testing Support
  - Generate initial test case outlines for:
    - Exchange request workflows
    - Model validation logic
    - View-level access control
  - Assist in refining pytest structure and fixture usage.
  - Support interpretation of failing tests and refactoring towards passing outcomes.
- ♿ Accessibility & UX
  - Provide guidance on:
    - Semantic HTML structure
    - Form labelling and error feedback
    - Keyboard navigation expectations
  - Assist with contrast and layout recommendations for readable UI.
- 📄 Documentation
  - Drafted and refined:
    - README structure and technical descriptions
    - User stories (MoSCoW prioritisation)
    - Feature summaries and setup instructions
  - Assisted in writing clear commit messages and pull request descriptions.

### Responsible AI Use

AI tools were used strictly as a development assistant, not as an autonomous code generator. All outputs were:

- Reviewed manually
- Adapted to project requirements
- Tested locally
- Integrated selectively

This approach reflects real-world software engineering workflows, where AI can be used as a productivity aid, not a replacement for developer understanding or accountability.

## Credits

- Django framework and documentation
- Bootstrap UI framework
- Heroku deployment platform
- Lighthouse auditing tool
- WAVE (WebAIM) accessibility evaluation tool
- AI tooling: GPT models and Claude models as per above section
