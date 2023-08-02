import falcon.asgi

from src.middlewares.auth import Auth
from src.middlewares.pool import Pool

from errors.storage import StorageError

from routes import suffix, users

app = falcon.asgi.App(middleware=[Pool(), Auth()])

users.routes(app)
suffix.routes(app)

app.add_error_handler(Exception, StorageError.handle)
