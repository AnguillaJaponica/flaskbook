from flask import Flask, current_app, g, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/hello/<name>")
def show_name(name):
    return render_template("index.html", name=name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        user_name = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # メールを送る
        # contactエンドポイントにリダイレクト
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


with app.test_request_context():
    # /
    # print(url_for("show_name"))
    # /hello/world
    # print(url_for("hello-endpoint", name="world"))
    # /hello/ichiro?page=1
    print(url_for("show_name", name="ichiro", page="1"))
