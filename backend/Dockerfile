FROM python:3

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

COPY . /app/

EXPOSE 8080

CMD ["uwsgi", "--http", ":8080", "--ini", "./uwsgi/uwsgi.ini"]
