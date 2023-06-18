import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def sys_path():
    return '<br>'.join(sys.path)