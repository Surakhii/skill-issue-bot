# syntax=docker/dockerfile:1

# Use a slim Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable stdout flush
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install runtime dependencies
# (Keep lean; add OS packages here only if your code needs them)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY bot.py /app/bot.py

# Default command
CMD ["python", "bot.py"]
