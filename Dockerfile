FROM python:3.8
LABEL MAINTAINER="Farshad"

ENV PYTHONUNBUFFERED 1

RUN mkdir /cv_app
WORKDIR /cv_app
COPY . /cv_app

ADD requirements.txt /cv_app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "coronaVirus", "--bind", ":8000", "coronaVirus.wsgi:application"]
