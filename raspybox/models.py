'''
Modelli
'''
from app import db
from flask_peewee.auth import BaseUser
from peewee import *
import datetime


class User(db.Model, BaseUser):
    '''
    Utente
    '''
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    def __unicode__(self):
        return self.username


class Device(db.Model):
    '''
    Dispositivo
    '''
    name = CharField()
    pin = IntegerField()
    
    def __unicode__(self):
        return self.name