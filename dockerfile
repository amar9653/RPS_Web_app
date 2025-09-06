# Use a Python base image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Copy your requirements file (or the whole project)
COPY requirements.txt .

# Install dependencies and create a virtual environment
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

# Set the virtual environment's bin directory in PATH
ENV PATH="/venv/bin:$PATH"

# Copy the rest of the project files
COPY . .

# Run Django migrations (this will use /venv/bin/python because of PATH)
RUN python manage.py makemigrations

# Default command to run the Django app (again uses /venv/bin/python because of PATH)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
