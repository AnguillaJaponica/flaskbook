from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello/<name>")
def show_name(name):
    return render_template("index.html", name=name)
