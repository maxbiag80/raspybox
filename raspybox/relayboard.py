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
        ic = int(channel)
        if (self.__isChannelActive(ic)):
            return "Power on relay on channel %d" % int(channel)
        else:
            return "Channel %d is not active" % ic
    
    def powerOff(self, channel):
        '''
        Power Off Relay
        @param channel: canale 
        '''
        ic = int(channel)
        if (self.__isChannelActive(ic)):
            return "Power off relay on channel %d" % int(channel)
        else:
            return "Channel %d is not active" % ic
        
    def status(self, channel):
        '''
        Get Relay Status
        @return status(0=Off, 1=On) 
        '''
        ic = int(channel)
        if (self.__isChannelActive(ic)):
            return "Get relay status on channel %d" % ic
        else:
            return "Channel %d is not active" % ic  
    
    def __isChannelActive(self, channel):
        self.__relays = Relay.select()
        for relay in self.__relays:
            if (relay.channel == int(channel)):
                return True
        return False