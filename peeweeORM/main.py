from peewee import *

db = PostgresqlDatabase('mydatabase', user='postgres', password='cs5421', host='localhost', port=5432)

class User(Model):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()

    class Meta:
        database = db


db.create_tables([User])


# insert row
user = User(username='john', password='secret', email='john@example.com')
user.save()


# get row
user = User.get(User.username == 'john')
print(user.email)

user = User.get(User.username == 'john')
user.password = 'new_password'
user.save()