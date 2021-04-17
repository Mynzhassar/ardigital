FROM python:3

ENV PYTHONUNBUFFERED 1

COPY backend/requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR /backend
COPY . /backend/

EXPOSE 8080

CMD ["uwsgi", "--http", ":8080", "--ini", "./uwsgi/uwsgi.ini"]
