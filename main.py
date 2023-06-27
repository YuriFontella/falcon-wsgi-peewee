import falcon, json

from pool import PoolMiddleware
from model import Users

class StorageError:
    @staticmethod
    def handle(e, req, resp, params):
        raise falcon.HTTPInternalServerError(description=str(e))

class AuthMiddleware:
	def process_request(self, req, resp):
		token = req.get_header('x-access-token')
		print(token)
                
def secure(req, resp, resource, params):
	print('Você está seguro')

@falcon.before(secure)
class UserResource:
    def on_get(self, req, resp):
        print(req.get_param('id', False))
        print(req.params)

        users = Users.select(Users.name).limit(1000).dicts()
        users = [user for user in users.iterator()]

        resp.media = users
    
    def on_post(self, req, resp):
        try:
            print(req.media)
            user = Users.insert(req.media).execute()
            resp.text = json.dumps(user)

        except Exception as e:
            raise Exception(e)

class SuffixResource:
	def on_get_all(self, req, resp):
		resp.text = 'all'

	def on_get_list(self, req, resp):
		resp.text = 'list'

app = falcon.App(middleware=[ PoolMiddleware(), AuthMiddleware()])

app.add_route('/users', UserResource())

app.add_route('/all', SuffixResource(), suffix='all')
app.add_route('/list', SuffixResource(), suffix='list')

app.add_error_handler(Exception, StorageError.handle)