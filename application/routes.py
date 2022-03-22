import imp
from . import app
from flask import Response


@app.route("/")
def entry_page():
    return Response({"Hello":"World!"},status=200)