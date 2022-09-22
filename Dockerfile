FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENV FLASK_APP ./app.py

CMD [ "python", "-m", "flask", "run" ]