import logging

from email_validator import EmailNotValidError, validate_email
from flask import (
    Flask,
    current_app,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "hogefugapiyo"
app.logger.setLevel(logging.DEBUG)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)
app.logger.critical("fatal error")
app.logger.critical("error")
app.logger.critical("warning")
app.logger.critical("info")
app.logger.critical("debug")


@app.route("/hello/<name>")
def show_name(name):
    return render_template("index.html", name=name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 入力チェック
        is_valid = True

        if not username:
            flash("ユーザ名は必須です")
            is_valid = False

        if not email:
            flash("メールは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # メールを送る
        # contactエンドポイントにリダイレクト
        flash("問い合わせ内容はメールにて送信しました。ありがとうございます。")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


with app.test_request_context():
    # /
    # print(url_for("show_name"))
    # /hello/world
    # print(url_for("hello-endpoint", name="world"))
    # /hello/ichiro?page=1
    print(url_for("show_name", name="ichiro", page="1"))
