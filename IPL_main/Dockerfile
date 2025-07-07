# Use full base Python image (not slim) for TensorFlow compatibility
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Install system dependencies (needed for scientific libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Flask/Gunicorn will use
EXPOSE 10000

# Start the Flask app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
