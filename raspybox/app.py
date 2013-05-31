'''
Modulo Applicazione
'''
from flask import Flask
from flask_peewee.db import Database
from relayboard import RelayBoard


"Crea nuovo oggetto applicazione"
app = Flask(__name__)
app.config.from_object('config.Configuration')

"Crea nuovo oggetto per l'accesso al database sqlite"
db = Database(app)

"Crea oggetto per la gestione della RelayBoard"
relayBoard = RelayBoard()