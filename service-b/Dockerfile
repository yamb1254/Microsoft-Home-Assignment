# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install Flask
RUN pip install flask

# Expose port 80
EXPOSE 80

# Command to run the Flask app
CMD ["python", "app.py"]
