FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/JamesLeeeeeee/django_1.git

WORKDIR /home/django_1/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-j_w+mg()iqmep&u5o$z)t+dgr^(1j(^e@2z4f+5@nj3l2iu)%*" > .env

WORKDIR /home/django_1/pinterest/

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8010

CMD ["gunicorn", "pinterest.wsgi", "--bind", "0.0.0.0:8010"]
