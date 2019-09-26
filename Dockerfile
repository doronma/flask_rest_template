# Pull a pre-built alpine docker image with nginx and python3 installed
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

# Set the port on which the app runs; make both values the same.
ENV LISTEN_PORT=5000
EXPOSE 5000

# Indicate where uwsgi.ini lives
ENV UWSGI_INI uwsgi.ini

# Tell nginx where static files live. Typically, developers place static files for
# multiple apps in a shared folder, but for the purposes here we can use the one
# app's folder. Note that when multiple apps share a folder, you should create subfolders
# with the same name as the app underneath "static" so there aren't any collisions
# when all those static files are collected together.
ENV STATIC_URL /rest_app/static

# Set the folder where uwsgi looks for the app
WORKDIR /app

# install required libs
COPY requirements.txt /app
RUN python3 -m pip install -r requirements.txt

# Copy the app contents to the image
COPY . /app



