from admin import admin
from api import api
from app import app
from models import *
import os


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

admin.setup()
api.setup()

def createTables():
    User.create_table(fail_silently=True)
    Device.create_table(fail_silently=True)


if __name__ == '__main__':
    createTables()
    app.run(host='0.0.0.0', port=8080, debug=True)
