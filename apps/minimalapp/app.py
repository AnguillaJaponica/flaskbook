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

app = Flask(__name__)
app.config["SECRET_KEY"] = "hogefugapiyo"


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
