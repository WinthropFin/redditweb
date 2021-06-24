FROM python:3.9.5
WORKDIR /usr/app
COPY ./ /usr/app
RUN apt-get update
RUN pip install -r requirements.txt

