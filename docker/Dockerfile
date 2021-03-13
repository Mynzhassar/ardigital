FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY requirements.txt/ /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /backend/
