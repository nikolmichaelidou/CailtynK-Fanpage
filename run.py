import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/characters.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="Meet the characters", characters=data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, for the feedback".format(request.form.get("name")))
        print(request.form["name"])
        print(request.form["email"])
        print(request.form["message"])
    return render_template("contact.html", page_title="Contact")


@app.route("/missions")
def missions():
    return render_template("missions.html", page_title="Her Story")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)
