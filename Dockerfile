FROM python:3.9-slim-buster

WORKDIR /usr/src/app

RUN apt update && apt install -y build-essential libpq-dev postgresql-client

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "server.py" ]
