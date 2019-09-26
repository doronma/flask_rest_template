import datetime

from flask import Flask  # Import the Flask class

app = Flask(__name__)    # Create an instance of the class for our use
print(f'{datetime.datetime.now()} Python flask init...')
