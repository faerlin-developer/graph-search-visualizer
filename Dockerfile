FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Disable Python buffering and enable Gunicorn
ENV PYTHONUNBUFFERED=1
EXPOSE 8050

CMD ["gunicorn", "--bind", "0.0.0.0:8050", "main:server"]
