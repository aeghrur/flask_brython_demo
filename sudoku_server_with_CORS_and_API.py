from flask import Flask, send_from_directory, request, abort
from flask_cors import CORS, cross_origin
from better_brython_app.sudoku import generate_sudoku

app = Flask(__name__, static_folder='C:/Users/xunliu/Documents/GitHub/python_webserver1/better_brython_app', static_url_path='')
cors = CORS(app)

@app.route("/api/sudoku_board")
def sudoku_board() -> str:
    if request.headers.get('username', '') == 'test_user':
        return(generate_sudoku(empty_str='0'))
    else:
        abort(401)

@app.route("/")
def hello_world():
    return send_from_directory('C:/Users/xunliu/Documents/GitHub/python_webserver1/better_brython_app', 'index.html')