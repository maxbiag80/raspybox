from models import Relay

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
        self.__relays = Relay.select()
        for relay in self.__relays:
            if (relay.channel == int(channel)):
                return "Relay: %s" % relay.device
         
#         return "Get relay status on channel %d" % int(channel)
        