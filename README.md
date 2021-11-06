# Python Flask Webserver Getting Started

This project was created for purposes of teaching students about \
Flask and getting started on using it in a simple manner. 

## Installation

Installation for Flask should be simple. For following this demo, \
please run the following:
pip install flask
pip install flask-cors

## Getting Started

First, let's organize our project. Create a folder called \
flask_webserver and we'll keep our flask related files here.

Next, let's create a file called server.py. This will be where \
we define our Flask routing functions. 

###Hello World

Alright, now we're ready to get started. In your server.py, add \
the following lines:

``
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'
``

Now, open up your command line and go to your flask_webserver folder.\
If you're on Windows, run ``set FLASK_APP=server`` and enter. \
If you're on Linux, run ``export FLASK_APP=server`` and enter. \
Then, run ``flask run`` and enter. 

You should now be able to go to localhost:5000 and see your server!