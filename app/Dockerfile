FROM python:3.11.1-bullseye

WORKDIR /usr/bin/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apt update & apt install python3-mysqldb
RUN pip install --upgrade pip
copy ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
