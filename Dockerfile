FROM python:3.10.7

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8001

CMD bash -c "python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8001 chew_and_cheer.wsgi"