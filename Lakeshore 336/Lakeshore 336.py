#!/usr/bin/env python

from VISA_Driver import VISA_Driver

__version__ = "0.0.1"

class Error(Exception):
    pass

class Driver(VISA_Driver):
    """ This class implements the Lakeshore 336 driver"""

    def performGetValue(self, quant, options={}):
        """Perform the get value operation"""
        if quant.name == 'PID P 1':
            reply = self.askAndLog('PID? 1')
            value,I,D = reply.split(',')
        elif quant.name == 'PID I 1':
            reply = self.askAndLog('PID? 1')
            P,value,D = reply.split(',')
        elif quant.name == 'PID D 1':
            reply = self.askAndLog('PID? 1')
            P,I,value = reply.split(',')
        elif quant.name == 'PID P 2':
            reply = self.askAndLog('PID? 2')
            value,I,D = reply.split(',')
        elif quant.name == 'PID I 2':
            reply = self.askAndLog('PID? 2')
            P,value,D = reply.split(',')
        elif quant.name == 'PID D 2':
            reply = self.askAndLog('PID? 2')
            P,I,value = reply.split(',')
        elif quant.name == 'Heater Mode 1':
            reply = self.askAndLog('OUTMODE? 1')
            value,input,powerup = reply.split(',')
        elif quant.name == 'Heater Input 1':
            reply = self.askAndLog('OUTMODE? 1')
            mode,value,powerup = reply.split(',')
        elif quant.name == 'Heater Mode 2':
            reply = self.askAndLog('OUTMODE? 2')
            value,input,powerup = reply.split(',')
        elif quant.name == 'Heater Input 2':
            reply = self.askAndLog('OUTMODE? 2')
            mode,value,powerup = reply.split(',')
        else:
            # General query
            value = self.askAndLog(quant.get_cmd)

        return value

    def performSetValue(self, quant, value, sweepRate=0.0, options={}):
        """Perform the set value operation"""
        if quant.name == 'PID P 1':
            # ask for curret values, so we don't overwrite I,D
            reply = self.askAndLog('PID? 1')
            P,I,D = reply.split(',')
            pidValues = '{:.1f},{},{}'.format(value,I,D)
            self.writeAndLog(quant.set_cmd + pidValues)
        elif quant.name == 'PID I 1':
            # ask for curret values, so we don't overwrite I,D
            reply = self.askAndLog('PID? 1')
            P,I,D = reply.split(',')
            pidValues = '{},{:.1f},{}'.format(P,value,D)
            self.writeAndLog(quant.set_cmd + pidValues)
        elif quant.name == 'PID D 1':
            # ask for curret values, so we don't overwrite I,D
            reply = self.askAndLog('PID? 1')
            P,I,D = reply.split(',')
            pidValues = '{},{},{:.1f}'.format(P,I,value)
            self.writeAndLog(quant.set_cmd + pidValues)
        elif quant.name == 'PID P 2':
            # ask for curret values, so we don't overwrite I,D
            reply = self.askAndLog('PID? 2')
            P,I,D = reply.split(',')
            pidValues = '{:.1f},{},{}'.format(value,I,D)
            self.writeAndLog(quant.set_cmd + pidValues)
        elif quant.name == 'PID I 2':
            # ask for curret values, so we don't overwrite I,D
            reply = self.askAndLog('PID? 2')
            P,I,D = reply.split(',')
            pidValues = '{},{:.1f},{}'.format(P,value,D)
            self.writeAndLog(quant.set_cmd + pidValues)
        elif quant.name == 'PID D 2':
            # ask for curret values, so we don't overwrite I,D
            reply = self.askAndLog('PID? 2')
            P,I,D = reply.split(',')
            pidValues = '{},{},{:.1f}'.format(P,I,value)
            self.writeAndLog(quant.set_cmd + pidValues)
        elif quant.name == 'Heater Mode 1':
            # ask for curret values, so we don't overwrite anything
            reply = self.askAndLog('OUTMODE? 1')
            mode,input,powerup = reply.split(',')

            index = quant.getValueIndex(value=value)
            heaterSetup = '{},{},{}'.format(index,input,powerup)
            self.writeAndLog(quant.set_cmd + heaterSetup)
        elif quant.name == 'Heater Input 1':
            # ask for curret values, so we don't overwrite anything
            reply = self.askAndLog('OUTMODE? 1')
            mode,input,powerup = reply.split(',')

            index = quant.getValueIndex(value=value)
            heaterSetup = '{},{},{}'.format(mode,index,powerup)
            self.writeAndLog(quant.set_cmd + heaterSetup)
        elif quant.name == 'Heater Range 1':
            index = quant.getValueIndex(value=value)
            self.writeAndLog(quant.set_cmd + str(index))
        elif quant.name == 'Heater Mode 2':
            # ask for curret values, so we don't overwrite anything
            reply = self.askAndLog('OUTMODE? 2')
            mode,input,powerup = reply.split(',')

            index = quant.getValueIndex(value=value)
            heaterSetup = '{},{},{}'.format(index,input,powerup)
            self.writeAndLog(quant.set_cmd + heaterSetup)
        elif quant.name == 'Heater Input 2':
            # ask for curret values, so we don't overwrite anything
            reply = self.askAndLog('OUTMODE? 2')
            mode,input,powerup = reply.split(',')

            index = quant.getValueIndex(value=value)
            heaterSetup = '{},{},{}'.format(mode,index,powerup)
            self.writeAndLog(quant.set_cmd + heaterSetup)
        elif quant.name == 'Heater Range 2':
            index = quant.getValueIndex(value=value)
            self.writeAndLog(quant.set_cmd + str(index))
        else:
            # The default precision of labber is too high...
            self.writeAndLog(quant.set_cmd + str(value))

        return value

if __name__ == '__main__':
    pass
