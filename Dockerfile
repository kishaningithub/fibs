FROM python:3.6.2
WORKDIR /app
COPY *.py .
CMD main.py
