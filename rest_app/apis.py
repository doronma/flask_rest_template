
from flask import Flask
from flask_restplus import Api, Resource

from . import app

api = Api(app)

@api.route('/hello_rest')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@app.route("/test")
def test():
    return "<html>this is a test</html>"

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
