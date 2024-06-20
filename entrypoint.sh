#!/bin/sh

# Wait for the PostgreSQL database to be ready
while ! nc -z db 5432; do
  echo "Waiting for the PostgreSQL database to be ready..."
  sleep 1
done

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth.models import User;
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'datapp123000!!!')
"

# Start the Django development server
exec "$@"
