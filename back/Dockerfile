FROM python:3.8.15-alpine

RUN apk update && apk add python3-dev gcc libc-dev

ENV DJANGO_SUPERUSER_PASSWORD=nicepassword
ENV DJANGO_SUPERUSER_EMAIL=djangoadmin@sysloan.com
ENV DJANGO_SUPERUSER_USERNAME=admin

WORKDIR /app

RUN pip install --upgrade pip
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./digitalsys_loan /app/digitalsys_loan

ADD ./server-entrypoint.sh /app/
ADD ./worker-entrypoint.sh /app/
RUN chmod +x ./server-entrypoint.sh
RUN chmod +x ./worker-entrypoint.sh
