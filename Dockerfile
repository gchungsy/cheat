# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY app.py .
COPY cheat_sheets/ ./cheat_sheets/

# Expose the port the app runs on
EXPOSE 5001

# Run the application with Gunicorn in production mode
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
