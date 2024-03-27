# pull official base image
FROM python:3.9.2-alpine


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN rm -rf /var/cache/apk/*

# install psycopg2 dependencies
RUN apk update \
    && apk add libffi-dev postgresql-dev wkhtmltopdf gcc python3-dev musl-dev py-pip jpeg-dev zlib-dev \
    && apk add libressl-dev perl rust libmagic pango openjpeg-dev g++


RUN apk --no-cache add \
    icu-dev \
    gettext \
    gettext-dev

RUN apk upgrade -U \
    && apk add ca-certificates ffmpeg \
    && rm -rf /var/cache/*


RUN apk --no-cache add glib-dev poppler-glib vips-dev vips-tools poppler-utils

COPY requirements/ .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r production.txt

# create directory for the app user

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

WORKDIR $APP_HOME

COPY . .


RUN ["chmod", "+x", "/home/app/web/entrypoint.sh"]
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
