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

@app.route("/poweron/<channel>")
def powerOn(channel):
    '''
    Power on relay
    @param channel: canale 
    '''
    return "Power on relay on channel %d" % int(channel)

@app.route("/poweroff/<channel>")
def powerOff(channel):
    '''
    Power off relay
    @param channel: canale 
    '''
    return "Power off relay on channel %d" % int(channel)