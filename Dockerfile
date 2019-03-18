FROM python:3.7

WORKDIR /work/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# RUN python manage.py collectstatic

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000

# $$$ TODO
# CMD exec gunicorn triahlonproject.wsgi --bind 0.0.0.0:8000
