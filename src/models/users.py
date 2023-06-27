import peewee

from config.db.pool import db

class Users(peewee.Model):
    id = peewee.IntegerField()
    name = peewee.CharField()
    group_id = peewee.IntegerField()

    class Meta:
        database = db