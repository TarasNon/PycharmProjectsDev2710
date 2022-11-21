from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return open(f"index.html").read()


app.run('localhost', debug=True, port=30000)
