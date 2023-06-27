import falcon, json

from src.models.users import Users
from src.hooks.secure import secure

@falcon.before(secure)
class UserResource:
    def on_get(self, req, resp):
        print(req.get_param('id', False))
        print(req.params)

        users = Users.select(Users.name).limit(1).dicts()
        users = [user for user in users.iterator()]

        resp.media = users
    
    def on_post(self, req, resp):
        try:
            print(req.media)
            user = Users.insert(req.media).execute()

            resp.status = falcon.HTTP_201
            resp.text = json.dumps(user)

        except Exception as e:
            raise Exception(e)