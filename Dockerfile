# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

#create container volume mounting to host dir so that the python script can read and write data from host
VOLUME /app/input
VOLUME /app/output

#creating preset  environment variables to be used used for the python script
ENV INPUT_DIR='/app/data/input'
ENV OUTPUT_DIR='/app/data/output'


# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Create input and output directories
RUN mkdir -p /app/data/input /app/data/output

# # Expose port (if needed)
# EXPOSE 8000

# Run the application
CMD ["python", "main.py"]