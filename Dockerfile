FROM python:3.10-slim AS base

WORKDIR /app

RUN apt-get update && \
    apt-get install -y nginx postgresql-client && \
    apt-get clean

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

RUN mkdir -p /app/staticfiles /app/logs

COPY . /app/

RUN python manage.py collectstatic --noinput

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
EXPOSE 8000

CMD ["sh", "-c", "service nginx start && gunicorn --workers 4 --timeout 120 --bind 0.0.0.0:8000 ai_prediction.wsgi:application"]