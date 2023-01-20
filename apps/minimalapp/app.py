from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/hello/<name>")
def show_name(name):
    return render_template("index.html", name=name)


with app.test_request_context():
    # /
    # print(url_for("show_name"))
    # /hello/world
    # print(url_for("hello-endpoint", name="world"))
    # /hello/ichiro?page=1
    print(url_for("show_name", name="ichiro", page="1"))
