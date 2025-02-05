# syntax=docker/dockerfile:1

FROM python:3.12.3-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
COPY bootstrap bootstrap
COPY app.py app.py

RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap"]
