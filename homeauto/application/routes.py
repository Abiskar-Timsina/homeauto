from . import app
from flask import Response,render_template


@app.route("/")
def entry_page():
    return render_template("home.html")