# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Flask and other dependencies
RUN apt-get update
RUN apt-get install -y gcc python3-dev
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]