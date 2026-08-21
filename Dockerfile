FROM python:3.11-slim

WORKDIR /app

COPY app.py .

# Run unbuffered to ensure live stdout logs in Kubernetes
ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
