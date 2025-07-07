# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files to the container
COPY . .

# Install system dependencies (optional, in case matplotlib, seaborn, etc. need it)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 10000

# Run the app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
