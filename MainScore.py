from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)


@app.route("/")
def score_():
    try:
        score_file = open("Scores.txt", "r")
        score_file.read()
        return render_template('score_good.html', SCORE=score_file)  # Open score details
    except FileNotFoundError or FileExistsError:  # If the file didn't open for any reason
        return render_template('score_bad.html', ERROR='Error')  # Prints error message


app.run()
