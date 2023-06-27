import peewee

from pool import db

class Users(peewee.Model):
    name = peewee.CharField()
    group_id = peewee.IntegerField()

    class Meta:
        database = db