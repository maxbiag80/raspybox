'''
Startup progetto
'''
from admin import admin
from api import api
from app import app
from models import *
from routes import *
import os

"Imposta path di avvio progetto"
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

"Configura console di amministrazione e modulo per effettuare le chiamate Restful"
admin.setup()
api.setup()

def createTables():
    '''
    Crea tabelle
    '''
    User.create_table(fail_silently=True)
    Relay.create_table(fail_silently=True)


if __name__ == '__main__':
    createTables()
    app.run(host='0.0.0.0', port=8080, debug=True)
