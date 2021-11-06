from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='C:/Users/xunliu/Documents/GitHub/python_webserver1/brython_app', static_url_path='')

@app.route("/")
def hello_world():
    return send_from_directory('C:/Users/xunliu/Documents/GitHub/python_webserver1/brython_app', 'index.html')