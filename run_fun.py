import responder
import backend.app as backapp

api = responder.API(debug=True, templates_dir='./dist', static_dir='./dist/static')

@api.route('/')
async def index(req, resp):
    resp.content = api.template('index.html')

@api.route('/api/login')
async def login(req, resp):
    isLogin = backapp.login(req.media())
    resp.media = {'login':isLogin}

if __name__ == '__main__':
    api.run()