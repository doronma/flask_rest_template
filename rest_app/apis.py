
import os

from flask import Flask
from flask_restplus import Api, Resource

from . import app

myName= os.environ.get('MY_NAME1')

api = Api(app)

@api.route('/hello_rest')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@app.route("/test")
def test():
    return f"<html>this is a test for {myName} </html>"

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
