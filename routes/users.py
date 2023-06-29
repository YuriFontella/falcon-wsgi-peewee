from src.controllers.users import UsersResource

user = UsersResource()

def routes(app):
    app.add_route('/users', user)
    app.add_route('/users/{id}', user, suffix='user')