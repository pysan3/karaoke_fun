import server.server as server

def login(data):
    name = data['user_name']
    password = data['user_password']
    return server.login(name, password)