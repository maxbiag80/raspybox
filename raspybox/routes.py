'''
Routing
'''
from app import app
from flask import send_from_directory
import os.path

@app.route('/favicon.ico')
def favicon():
    '''
    Favicon
    '''
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')
    
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