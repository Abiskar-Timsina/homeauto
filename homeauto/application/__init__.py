from flask import Flask

app = Flask(__name__,template_folder="static")

from . import routes