import falcon

class AuthMiddleware:
    def process_request(self, req, resp):
        token = req.get_header('x-access-token')
        print(token)

        if token is None:
            raise falcon.HTTPUnauthorized(title='Unauthorized', description='Invalid token')