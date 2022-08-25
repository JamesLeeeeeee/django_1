FROM python:3.9.0

WORKDIR /home/

RUN echo "ts"

RUN git clone https://github.com/JamesLeeeeeee/django_1.git

WORKDIR /home/django_1/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

WORKDIR /home/django_1/pinterest/

RUN python manage.py collectstatic

EXPOSE 8010

CMD ["bash", "-c", "python manage.py migrate --settings=pinterest.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=pinterest.settings.deploy pinterest.wsgi --bind 0.0.0.0:8010"]

