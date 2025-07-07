FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools wheel
RUN pip cache purge
RUN pip install -r requirements.txt

EXPOSE 10000

CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "--timeout", "120", "app:app"]
