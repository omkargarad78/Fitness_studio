# 🏋️‍♀️ Fitness Class Booking App

A full-stack Python project that allows users to view and book fitness classes such as Yoga, Zumba, and HIIT. Built using **FastAPI** for the backend, **SQLite** for the database, and **Streamlit** for the frontend. The entire application can be run in a single Docker container using Supervisor.

---

## 🚀 Features

- View upcoming fitness classes (name, instructor, date/time, available slots)
- Book a class by providing name and email
- Check your past bookings using your email
- Proper input validation and error handling
- Streamlit-based frontend with a modern UI
- All-in-one Docker setup (no need to run separate terminals)

---

## 🧱 Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Database**: SQLite (via SQLAlchemy)
- **API Validation**: Pydantic
- **Process Management**: Supervisor
- **Containerization**: Docker

---

## 🗂️ Project Structure

```text
Omnify_Assignment/
├── backend/
│   ├── main.py          # FastAPI entry point
│   ├── models.py        # SQLAlchemy models (tables)
│   ├── crud.py          # DB logic (CRUD)
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # DB engine and session
│   └── __init__.py
│
├── frontend/
│   └── app.py           # Streamlit frontend
│
├── supervisord.conf     # Supervisor config to run both services
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build file
└── README.md            # Project documentation
```



---

## ⚙️ Getting Started

### ✅ 1. Run with Docker (Recommended)

Make sure Docker is installed.

```bash
docker build -t omnify-app .
docker run -p 8000:8000 -p 8501:8501 omnify-app
```

⛳ Access the App:
Frontend (Streamlit): http://localhost:8501

Backend (FastAPI docs): http://localhost:8000/docs

---
🔧 2. Run Manually (Without Docker)
Create and Activate the virtual environment

```
python -m venv env
env/Scripts/Activate
```

Install all the required dependencies
```
pip install -r requirements.txt
```

Run backend first using command
```
uvicorn backend.main:app --reload
```

Run Frontend
Open a new termianl, activate virtual environment and Execute:
```
streamlit run froentend/app.py
```

Open the Front end and perform CRUD operations
