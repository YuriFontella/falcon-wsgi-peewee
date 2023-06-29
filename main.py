import falcon

from src.middlewares.auth import AuthMiddleware
from src.middlewares.pool import PoolMiddleware

from errors.storage import StorageError

from routes import suffix, users

app = falcon.App(middleware=[PoolMiddleware(), AuthMiddleware()])

users.routes(app)
suffix.routes(app)

app.add_error_handler(Exception, StorageError.handle)
