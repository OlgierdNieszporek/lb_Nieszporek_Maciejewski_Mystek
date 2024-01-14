from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "5003 - Myszkow jest wspaniale"


if __name__ == '__main__':
    app.run(port=5003, debug=True)
