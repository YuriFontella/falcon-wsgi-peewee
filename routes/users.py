from src.controllers.user import UserResource

user = UserResource()

def routes(app):
    app.add_route('/users', user)
    app.add_route('/users/{id}', user, suffix='user')