# flask_rest_template
Very simple flask api application, ready to be Dockerized.

build:
docker build --rm -f "Dockerfile" -t user/simple-flask-rest:latest .

run:
docker run --rm -it -p 5000:5000/tcp user/simple-flask-rest:latest

run locally:
export FLASK_APP=rest_app.webapp
/home/doron/Projects/git-projects/flask_rest_template/venv/bin/flask run
