from playhouse.pool import PooledPostgresqlDatabase

db = PooledPostgresqlDatabase('blocks', user='postgres', password='123456', host='localhost', max_connections=8, stale_timeout=300)

class PoolMiddleware:
    def process_request(self, req, resp):
        db.connect()

    def process_response(self, req, resp, resource, params):
        db.close()
