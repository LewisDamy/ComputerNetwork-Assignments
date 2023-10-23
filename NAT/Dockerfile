# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python server code to the container
COPY server.py /app/server.py

# Install required Python libraries
# RUN pip install requests

# Expose port 12345 for the server
EXPOSE 12345

# Define the environment variable for the IPinfo API key
# ENV IPINFO_API_KEY your_api_key_here

# Start the Python server when the container runs
CMD ["python", "server.py"]
