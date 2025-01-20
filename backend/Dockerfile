FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY . .

# Expose the Flask port
EXPOSE 8080

# Set the environment variable to make Flask accessible
ENV FLASK_RUN_HOST=0.0.0.0

# Default command
CMD ["python", "app.py"]
