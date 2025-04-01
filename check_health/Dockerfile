FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./check_health

CMD ["uvicorn", "check_health.main:app", "--host", "0.0.0.0", "--port", "8080"]