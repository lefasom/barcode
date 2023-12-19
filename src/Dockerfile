# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN apt-get update && apt-get install -y libzbar-dev
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run flask when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
