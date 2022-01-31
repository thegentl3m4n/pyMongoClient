FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /demo
WORKDIR /demo
RUN pip install pymongo
CMD python mongo_client.py