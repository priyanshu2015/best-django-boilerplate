FROM python:3.8


RUN mkdir -p /usr/app/
WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements/development.txt .
RUN pip install -r requirements/development.txt

COPY . .