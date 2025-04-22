
# Student Performance Visualization App

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

A Streamlit web application that visualizes student performance data from an SQLite database, containerized with Docker.

## Features

- 📊 Interactive dashboard with grade filtering
- 📈 Visual performance metrics with bar charts
- 🎲 Sample dataset of 1200 randomly generated records
- 🐳 Dockerized deployment with data persistence
- 🛠️ Easy local development setup

## Quick Start

### With Docker (Recommended)

```bash
docker-compose up --build
```
Access the app at: http://localhost:8501

### Local Development

1. Set up virtual environment:
```bash
python -m venv .venv
# Activate:
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Generate sample data:
```bash
python generate_data.py
```

4. Run the app:
```bash
streamlit run app.py
```

## Project Structure

```
student_performance_app/
├── app.py              # Main Streamlit application
├── generate_data.py    # Data generation script
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker orchestration
├── requirements.txt    # Python dependencies
└── students.db         # SQLite database (auto-generated)
```

## Configuration

Customize these environment variables in `docker-compose.yml` if needed:

- `PORT`: Change the default port (8501)
- `PYTHONUNBUFFERED`: Set to 1 for better logging

## Technologies Used

- Python 3.9
- Streamlit
- SQLite
- Docker + Docker Compose
- Faker library (for test data)

