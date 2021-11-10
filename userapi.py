import time

from flask import request, session, redirect, Blueprint

userapi = Blueprint('userapi', __name__,
                      template_folder='templates')
SESSION_EXPIRE_TIME=7200

@userapi.route('/username')
def username():
    return session['username']

@userapi.before_request
def load_user():
    if "username" in session and "timestamp" in session:
        try:
            if int(session['timestamp']) + SESSION_EXPIRE_TIME > int(time.time()):
                return None
        except:
            return "Malformed session"
        return redirect("/index.html", code=302)
