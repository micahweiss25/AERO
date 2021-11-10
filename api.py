import threading
import time

from flask import request, session, redirect, Blueprint

from push_notifs import getDiscordChatBot

publicapi = Blueprint('api', __name__,
                      template_folder='templates')

from db import verifyUserPass


@publicapi.route('/version')
async def hello_world():
    await getDiscordChatBot().sendTestMessage("yo")
    return 'aquaponics 0.0.0'


@publicapi.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if  username!=None and password!=None and verifyUserPass(username, password):
        session['username'] = username
        session['timestamp'] = int(time.time())
        return redirect("/dashboard", code=302)
    return "Login Invalid"