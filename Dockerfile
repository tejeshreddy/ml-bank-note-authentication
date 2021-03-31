FROM python:3.8-slim-buster

COPY . /usr/app

WORKDIR /usr/app

RUN pip install -r requirements.txt

CMD python flasgger_app.py
