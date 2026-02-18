# Running FastAPI Project

This guide explains how to run the FastAPI project on any machine using **Python** or **Docker**.

---

## 1. Clone the Repository

```bash
git clone https://github.com/xjojoramirez/fastapi-start.git
cd fastapi-start


Option 1: Run using Python + Virtual Environment

Create a virtual environment:
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate     # Windows

Install dependencies:
pip install --upgrade pip
pip install -r requirements.txt

Run the FastAPI server:
uvicorn app.main:app --reload

Open in your browser:
http://127.0.0.1:8000/docs
The Swagger UI allows you to test all endpoints directly.

Option 2: Run using Docker

Build the Docker image:
docker build -t fastapi-start .

Run the container:
docker run -d -p 8000:8000 fastapi-start

Open in browser:
http://127.0.0.1:8000/docs

To stop the container:
docker ps          # find container ID
docker stop <id>
