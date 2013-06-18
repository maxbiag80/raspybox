from common import *
from models import Relay
import serial


class RelayBoard:
    '''
    Relay Board Manager
    '''
    
    def powerOn(self, channel):
        '''
        Power On Relay
        @param channel: canale 
        @return: status
        '''
        ic = int(channel)
        if (self.__isChannelActive(ic)):
            self.__sendCommand(ic, ON)
            return self.status(channel);
        else:
            return CHANNEL_NOT_ACTIVE
    
    def powerOff(self, channel):
        '''
        Power Off Relay
        @param channel: canale 
        @return: status
        '''
        ic = int(channel)
        if (self.__isChannelActive(ic)):
            self.__sendCommand(ic, OFF)
            return self.status(channel);
        else:
            return CHANNEL_NOT_ACTIVE
    
    def status(self, channel):
        '''
        Get Relay status
        @param channel: canale 
        @return: status
        '''
        ic = int(channel)
        if (self.__isChannelActive(ic)):
            status = self.__sendCommand(ic, STATUS)
            return status
        else:
            return CHANNEL_NOT_ACTIVE       
    
    def __isChannelActive(self, channel):
        self.__relays = Relay.select()
        for relay in self.__relays:
            if (relay.channel == int(channel)):
                return True
        return False
    
    def __sendCommand(self, channel, command):
        "ser = serial.Serial(RELAY_BOARD_COM_PORT)"
        
        """
        Comandi:
        
        FIRST chanel commands:
        OFF command : FF 01 00 (HEX) or 255 1 0 (DEC)
        ON command : FF 01 01 (HEX) or 255 1 1 (DEC)
        SECOND chanel commands:
        OFF command : FF 02 00 (HEX) or 255 2 0 (DEC)
        ON command : FF 02 01 (HEX) or 255 2 1 (DEC)
        THIRD chanel commands:
        OFF command : FF 03 00 (HEX) or 255 3 0 (DEC)
        ON command : FF 03 01 (HEX) or 255 3 1 (DEC)
        FOURTH chanel commands:
        OFF command : FF 04 00 (HEX) or 255 4 0 (DEC)
        ON command : FF 04 01 (HEX) or 255 4 1 (DEC)
        FF 09 00 - Status request command
        > xx xx xx xx  - Reply from relay where xx is status: 01 - Relay is ON, 00 - Relay is OFF
        First byte is status first relay, Fourth byte is status fourth relay
        """                                          
        if (STATUS == command):
            "buffer = ser.read(chr(255) + chr(command) + chr(0));"
            buffer = "0000"
            return self.__parseStatus(buffer, channel);
        else:
            "ser.write(chr(255) + chr(channel) + chr(command))"
        
        "ser.close()"
    
    def __parseStatus(self, buffer, channel):
        return 1;