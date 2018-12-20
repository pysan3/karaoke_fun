from database import *

def login(name, password):
    session = Session()
    user = session.query(Users).filter(Users.user_name==name).all()
    if len(user) == 1:
        if user.user_password == password:
            return 'true'
        else:
            return 'false'
    elif len(user) == 0:
        return 'no users'
    else:
        return 'too many users'

def main():
    session = Session()
    session.add(Eventlogs())