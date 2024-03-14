FROM python:3.12.2

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN addgroup --system app && adduser --system --group app

RUN pip install --upgrade pip  

COPY . /app
RUN chown -R app:app /app

RUN pip install -r requirements-prod.txt
RUN python manage.py collectstatic --noinput --clear

EXPOSE 8080

USER app:app

CMD gunicorn oc_lettings_site.wsgi:application -b 0.0.0.0:8080 --workers 4