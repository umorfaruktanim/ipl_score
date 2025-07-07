# Use full Python 3.10 image for compatibility
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy only requirements.txt first (for better caching)
COPY requirements.txt requirements.txt

# Copy the rest of the application code
COPY . .

# Install system dependencies required by scientific packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel and clear pip cache
RUN pip install --upgrade pip setuptools wheel
RUN pip cache purge

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port your app listens on (10000 as per your config)
EXPOSE 10000

# Command to start the Flask app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
