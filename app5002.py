from datetime import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "5002"


if __name__ == '__main__':
    app.run(port=5002, debug=True)
