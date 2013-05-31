class RelayBoard:
    '''
    Relay Board Manager
    '''
    def powerOn(self, channel):
        '''
        Power On Relay
        @param channel: canale 
        '''
        return "Power on relay on channel %d" % int(channel)
    
    def powerOff(self, channel):
        '''
        Power Off Relay
        @param channel: canale 
        '''
        return "Power off relay on channel %d" % int(channel)
    
    def status (self, channel):
        '''
        Get Relay Status
        @return status(0=Off, 1=On) 
        '''
        return "Get relay status on channel %d" % int(channel)