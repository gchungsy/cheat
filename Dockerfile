# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY app.py .

# Expose the port the app runs on
EXPOSE 5000

# Run the application in non-debug mode
CMD ["python", "app.py"]
