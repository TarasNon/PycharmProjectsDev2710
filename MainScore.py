from flask import Flask, render_template


app = Flask(__name__, template_folder='.')


@app.route("/")
def score():
    try:
        score_file = open("Score.txt", "r")
        score_ = score_file.read()
        return render_template("score.html", SCORE=score_)
    except FileNotFoundError or FileExistsError:
        return render_template('score_bad.html', ERROR='Error')


app.debug = True
app.run()
