from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/answer", methods=["POST"])
def answer():
    user_answer = request.form.get("answer")
    if user_answer == "yes":
        return render_template("lose.html")
    else:
        return render_template("win.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)