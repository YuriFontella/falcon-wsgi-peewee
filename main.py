import falcon

from src.middlewares.auth import AuthMiddleware
from src.middlewares.pool import PoolMiddleware

from routes import users, suffix

class StorageError:
    @staticmethod
    def handle(e, req, resp, params):
        raise falcon.HTTPInternalServerError(description=str(e))

app = falcon.App(middleware=[ PoolMiddleware(), AuthMiddleware()])

users.routes(app)
suffix.routes(app)

app.add_error_handler(Exception, StorageError.handle)