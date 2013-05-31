'''
Modulo gestione chiamate Restful
Es.: http://localhost:8080/api/device/
'''
from app import app
from auth import auth
from flask_peewee.rest import RestAPI, RestResource, UserAuthentication, \
    AdminAuthentication
from models import User, Device


class UserResource(RestResource):
    '''
    Gestione risorse User
    Consente di configurare i campi esportati nel json
    '''
    exclude = ('password', 'email',)

"Configura Authenticator per User e Admin"
user_auth = UserAuthentication(auth)
admin_auth = AdminAuthentication(auth)

"Crea oggetto API per la gestione delle chiamate Restful"
api = RestAPI(app, default_auth=user_auth)

"Registra Modelli"
api.register(User, UserResource, auth=admin_auth)
api.register(Device)
