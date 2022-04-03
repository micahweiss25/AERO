import configparser
import time

from flask import Flask


from api import publicapi
from db import *

from flask import g
import secrets

from devstaticpageserver import spages
from push_notifs import startDiscordBot, getDiscordChatBot
from userapi import userapi

app = Flask(__name__)
app.register_blueprint(publicapi, url_prefix='/api')
app.register_blueprint(userapi, url_prefix='/api/user')
app.register_blueprint(spages, url_prefix='/')

app.config['SECRET_KEY'] = secrets.token_urlsafe(24)


configuration = configparser.ConfigParser()
configuration.read("config.ini")

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


with app.app_context():
    init_db()
    if get_db().execute("SELECT * FROM users").fetchone():
        pass
    else:
        newpass = secrets.token_urlsafe(13)
        print(f"The default login is 'admin' and password '{newpass}'")
        createUser("admin", True, newpass)
    startDiscordBot()

if __name__ == '__main__':
    app.run()
