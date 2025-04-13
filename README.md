# Advanced FastAPI Blog Application

A high-performance blog backend built with FastAPI, PostgreSQL, and modern Python.

## Features

- 🚀 **FastAPI-powered** with async support
- 🔐 JWT Authentication (OAuth2 with password flow)
- 📝 CRUD operations for blog posts
- 🏷️ Tag/Category system
- ✨ Advanced features:
  - Rate limiting
  - Caching
  - Background tasks (email notifications)

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL 
- **Authentication**: JWT
- **Cache**: Redis
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL 13+
- Redis (for caching)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-blog.git
   cd fastapi-blog

2. Create a virtual environment:
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate    # Windows

3. Install dependencies:
    
    pip install -r requirements.txt

4. Set up environment variables:
    cp .env.example .env
    Edit .env with your configuration.

    Run migrations:
    alembic upgrade head

5. Running the Application
    Development

    uvicorn app.main:app --reload

6. Production
    gunicorn -k uvicorn.workers.UvicornWorker app.main:app

API Documentation

After starting the server, access interactive docs:

    Swagger UI: http://localhost:8000/docs

    ReDoc: http://localhost:8000/redoc

Endpoints
Method	Endpoint	Description	Auth Required
POST	/auth/token	Get JWT token	No
POST	/posts/	Create new post	Yes
GET	/posts/	List all posts	No
GET	/posts/{post_id}	Get single post	No
PUT	/posts/{post_id}	Update post	Yes
DELETE	/posts/{post_id}	Delete post	Yes

## Deployment
### Docker

docker-compose up --build

# License
MIT
<div align="center"> <sub>Built with ❤︎ by <a href="https://github.com/HosseinSiw">Hossein siadati</a></sub> </div> ```
