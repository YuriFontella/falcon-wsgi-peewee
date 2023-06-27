from src.controllers.user import UserResource

def routes(app):
    app.add_route('/users', UserResource())