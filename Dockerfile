FROM python:3.7

WORKDIR /build
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . .

EXPOSE 8000
CMD gunicorn -w 4 triahlonproject.wsgi --bind 0.0.0.0:8000
