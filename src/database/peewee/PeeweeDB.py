import datetime

from peewee import *

USER = 'postgres'
PASSWORD = '2558444saw'
HOST = 'localhost'
PORT = 5432
DATABASE = 'mirolagram'

db = PostgresqlDatabase(
                DATABASE,
                user=USER, 
                password=PASSWORD,
                host=HOST,
                port=PORT)


# MODELS
class UserPeewee(Model):
    id = AutoField()
    idIG = TextField(unique=True)
    username = TextField(unique=True)
    name = TextField()
    image = TextField(null=True)
    createdAt = DateTimeField(default=datetime.datetime.now)
    isNew = BooleanField(default=True)
    
    class Meta:
        table_name = 'users'
        database = db
        
db.connect()
db.create_tables([UserPeewee])