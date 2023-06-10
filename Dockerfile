FROM python:3.11-slim

# Path: /app
WORKDIR /app

# Path: /app/requirements.txt
COPY requirements.txt .

# Path: /app
COPY /app .

# Path: /app
RUN pip install -r requirements.txt

# Path: /app
CMD ["python", "-u", "main.py"]
