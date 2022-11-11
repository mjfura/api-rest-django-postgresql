FROM python:3.11.0-slim-buster

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .