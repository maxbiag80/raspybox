from app import app
from auth import auth
from flask_peewee.rest import RestAPI, RestResource, UserAuthentication, \
    AdminAuthentication
from models import User, Device


user_auth = UserAuthentication(auth)
admin_auth = AdminAuthentication(auth)

api = RestAPI(app, default_auth=user_auth)


class UserResource(RestResource):
    exclude = ('password', 'email',)


class DeviceResource(RestResource):
    owner_field = 'user'
    include_resources = {'user': UserResource}


api.register(User, UserResource, auth=admin_auth)
api.register(Device)
