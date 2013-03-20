'''
Modulo di Amministrazione
'''
from app import app
from auth import auth
from flask_peewee.admin import Admin, ModelAdmin
from models import Device


class DeviceAdmin(ModelAdmin):
    '''
    Amministrazione Model Device
    '''
    columns = ('name', 'pin',)

"Crea oggetto Admin associandolo ad un'Authenticator"
admin = Admin(app, auth)
auth.register_admin(admin)

"Registra Model"
admin.register(Device, DeviceAdmin)