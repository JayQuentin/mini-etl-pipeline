# BAsic Image with Python
FROM python:3.9

# Set Working directory in Container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Code & Data into Container Image
COPY . .

# Start ETL Job
CMD ["python", "app/main.py"]

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3