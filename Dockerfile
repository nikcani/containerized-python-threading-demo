FROM python:3-slim

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED 1

CMD ["python", "demo.py"]
