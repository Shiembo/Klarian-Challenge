# Use the official Python image from the Docker Hub
FROM python:3.12

# Prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install PostgreSQL client
RUN apt-get update && apt-get install -y \
    netcat-traditional \
    postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the codebase into the working directory
COPY . .

# Ensure the entrypoint.sh script has executable permissions
RUN chmod +x /code/entrypoint.sh

# Expose port 8000 to access the Django app
EXPOSE 8000

# Use the custom entrypoint script
ENTRYPOINT ["/code/entrypoint.sh"]

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

