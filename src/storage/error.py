import falcon

class Error:
    @staticmethod
    def handle(e, req, resp, params):
        raise falcon.HTTPInternalServerError(description=str(e))