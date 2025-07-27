# 🔗 ShortenerAPI – Simple URL Shortener with FastAPI

A minimal and fast URL shortener API built with **FastAPI** and **SQLite**, inspired by Bit.ly.  
It allows users to generate short URLs and automatically redirect to the original links.

---

## 🚀 Features

- Shorten any valid URL with a single endpoint
- Fast redirection using unique short codes
- Click counter per URL (optional)
- Fully tested with `pytest`
- Dockerized for easy deployment

---

## 🧱 Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Database**: SQLite
- **Testing**: Pytest + TestClient
- **Containerization**: Docker, Docker Compose

---

## 📦 Project Structure

ShortenerAPI/
├── app/
│ ├── main.py # Entry point
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # DB connection
│ ├── utils.py # Code generator
│ └── routes/
│ └── url.py # API routes
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── test_main.py # Tests

## 🧪 Local Development

### 1. Create virtual environment and install dependencies

```bash
python -m venv env
source env/bin/activate       # Linux/macOS
env\Scripts\activate          # Windows

pip install -r requirements.txt

2. Run the server

uvicorn app.main:app --reload
Visit: http://localhost:8000/docs


Docker Usage
1. Build the container
docker-compose build
2. Run the container
docker-compose up

API will be available at: http://localhost:8000