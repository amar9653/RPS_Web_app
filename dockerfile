FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \ 
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m venv venv

RUN Source/venv/bin/activate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
