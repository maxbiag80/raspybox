class Configuration(object):
    DATABASE = {
        'name': 'data/raspybox.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    DEBUG = True
    SECRET_KEY = 'qwertyuiop'
