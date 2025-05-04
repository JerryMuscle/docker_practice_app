FROM ubuntu:22.04

RUN apt update && \
    apt install -y python3-pip
RUN pip3 install Flask Flask-SQLAlchemy
RUN apt clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /book_app

COPY . .

CMD ["python3", "main.py"]