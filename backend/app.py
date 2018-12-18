import sqlite3

import server.server as server
from server.database import Session

def login(data):
    name = data['user_name']
    password = data['user_password']
    return server.login(name, password)