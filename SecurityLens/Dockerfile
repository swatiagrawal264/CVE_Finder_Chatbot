# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Run migrations and collect static files (if necessary)
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
