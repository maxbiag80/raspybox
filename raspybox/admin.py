from app import app
from auth import auth
from flask_peewee.admin import Admin, ModelAdmin
from models import Device


class DeviceAdmin(ModelAdmin):
    columns = ('name', 'pin',)

admin = Admin(app, auth)

auth.register_admin(admin)
admin.register(Device, DeviceAdmin)