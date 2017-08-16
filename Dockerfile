FROM python:3.6.2-alpine
WORKDIR /app
COPY *.py ./
CMD main.py
