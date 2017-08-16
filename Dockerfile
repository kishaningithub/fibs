FROM python:3.6.2-alpine
WORKDIR /app
COPY *.py ./
CMD ["python", "main.py"]
