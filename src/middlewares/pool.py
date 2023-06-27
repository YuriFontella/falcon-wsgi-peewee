from config.db.pool import db

class PoolMiddleware:
    def process_request(self, req, resp):
        db.connect()

    def process_response(self, req, resp, resource, params):
        db.close()