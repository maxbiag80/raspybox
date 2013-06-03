'''
Routing
'''
from app import app, appModules
from common import *
from flask import send_from_directory
import os.path


@app.route('/favicon.ico')
def favicon():
    '''
    Favicon
    '''
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')
    
@app.route("/poweron/<channel>")
def powerOn(channel):
    '''
    Power on relay
    @param channel: canale 
    '''
    relayBoard = appModules[MODULE_RELAY_BOARD]
    return relayBoard.powerOn(channel);

@app.route("/poweroff/<channel>")
def powerOff(channel):
    '''
    Power off relay
    @param channel: canale 
    '''
    relayBoard = appModules[MODULE_RELAY_BOARD]
    return relayBoard.powerOff(channel);

@app.route("/status/<channel>")
def status(channel):
    '''
    Get Relay Status
    @return status(0=Off, 1=On) 
    '''
    relayBoard = appModules[MODULE_RELAY_BOARD]
    return relayBoard.status(channel);