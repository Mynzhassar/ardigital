FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY requirements/ /tmp/requirements
RUN pip install -r /tmp/requirements/base.txt
COPY . /backend/
