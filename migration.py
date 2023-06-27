import peewee

from model import Users

from pool import db

try:
    Users.create_table()
except peewee.OperationalError as e:
  	print(e)

def create_tables():
   with db:
        db.create_tables([Users])