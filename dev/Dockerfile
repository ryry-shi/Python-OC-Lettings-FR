FROM python:3.12.2

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY .. /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt