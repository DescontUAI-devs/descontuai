FROM python:3.6-alpine
ADD . /web
WORKDIR /web
RUN pip install -r requirements.txt