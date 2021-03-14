FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY requirements/base.txt/ /tmp/requirements/base.txt
RUN pip install -r /tmp/requirements/base.txt
COPY . /backend/
