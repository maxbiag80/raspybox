'''
Web Services
'''
from app import app


@app.route("/test/")
def test():
    '''
    Servizio di test
    Utilizzato per testare il corretto funzionamento dell'applicativo
    '''
    return "Test Service OK!"