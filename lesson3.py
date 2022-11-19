from flask import Flask


app = Flask(__name__)

@app.route('/content')
def read():
    return open("words.txt").read(), 200


@app.route('/register')
def register():
    return open("read.txt", 'r').read()
    return "success", 201

if __name__ == '__main__':
    app.run('localhost', debug=True, port=30000)
