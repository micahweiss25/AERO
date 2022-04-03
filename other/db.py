import sqlite3

from flask import g

import crypto

DATABASE = './database.db'

def init_db():
    db = get_db()
    with open('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def createUser(username : str, isAdmin : bool, password : str) -> bool:
    if userWithName(username):
        return True
    get_db().execute("INSERT INTO users VALUES (?,?,?,?)",
                     (None, username, isAdmin, crypto.generatePasswordHash(password)))
    get_db().commit()
    return True

def userWithName(username: str) -> bool:
    if get_db().execute("SELECT username FROM users WHERE username = ?", (username,)).fetchone():
        return True
    return False
def verifyUserPass(username : str, password : str) -> bool:
    passhash = get_db().execute("SELECT phash FROM users WHERE username = ?", (username,)).fetchone()[0]
    if crypto.verifyPasswordHash(password, passhash):
        return True
    return False

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db