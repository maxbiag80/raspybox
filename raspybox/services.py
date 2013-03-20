'''
Web Services
'''
from app import app


@app.route("/test/<signal>")
def test(signal):
    '''
    Servizio di test
    Utilizzato per testare il corretto funzionamento dell'applicativo
    '''
    return "Test Service OK! Signal=%s" % signal