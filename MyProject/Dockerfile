# Use an official Python runtime as the base image (Python Version 3.10.x)
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /apps

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code from current folder, to the container's /apps/ folder
COPY . .

# Set the command to run the microservice/app (This uses the Python 3.10.x interpreter)
CMD [ "python", "my_app/app.py" ]
