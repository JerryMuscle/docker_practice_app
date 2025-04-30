FROM python:3.11-slim

WORKDIR /book_app
RUN pip install Flask Flask-SQLAlchemy

CMD ["python", "main.py"]