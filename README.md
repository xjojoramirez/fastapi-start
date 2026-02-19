
# FastAPI CRUD App

A simple CRUD API built with FastAPI and SQLAlchemy, containerized with Docker.

---

## �� Features

- Create items
- Read all items
- Read single item
- Update item
- Delete item
- SQLite database
- Dockerized setup
- Swagger documentation

---

## �� Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Docker
- Docker Compose

---

## �� Project Structure

fastapi-start/
├── Dockerfile
├── docker-compose.yml
├── app/
│ ├── crud.py
│ ├── database.py
│ ├── main.py
│ ├── models.py
│ └── schemas.py
└── requirements.txt


---

## ▶️ Run with Docker (Recommended)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/xjojoramirez/fastapi-start.git

cd fastapi-start

docker compose up -d --build

http://localhost:8027/docs
