# Use Alpine as the base image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Install dependencies and build tools required for certain Python packages
RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    bash \
    curl

# Install FastAPI and Uvicorn dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files to the container
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI app using Uvicorn
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
