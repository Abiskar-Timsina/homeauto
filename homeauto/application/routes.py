from . import app
from flask import Response,render_template,request
from . import utils
from decouple import config
import redis


redis_server = redis.Redis(host=config("redis_server"),port=config("redis_port"))

@app.route("/")
def entry_page() -> render_template:
    """
    Returns the home page for the project
    """
    return render_template("home.html")

@app.route("/send")
def send_page() -> render_template:
    """
    Returns the send message page for now
    """
    token = utils.Token().gen_token()
    redis_server.setex(token,30,token)
    return render_template("message.html",token=token)

@app.route("/sendapi",methods=["POST"])
def recv_msg() -> Response:
    """
    Returns the response to the send message
    """
    if request.content_type == "application/x-www-form-urlencoded":
        recieved_token = request.form.get('token')

        if redis_server.exists(recieved_token):
            redis_server.delete(recieved_token)
            print(request.form.get('message'))
            return Response("Done!",status=200)
        else:
            return Response("User not in session",status=401)
        
    return Response("Bad Request",status=400)