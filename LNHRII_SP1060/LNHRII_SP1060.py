from VISA_Driver import VISA_Driver
import struct

class Driver(VISA_Driver):

    def performOpen(self, options={}):
        VISA_Driver.performOpen(self, options)
        sAns = self.askAndLog('ALL ON\n')
        return sAns

    def performClose(self, bError=False, options={}):
        VISA_Driver.performClose(self, bError, options=options)
        pass

    def performGetValue(self, quant, options={}):
        """Perform the Get Value instrument operation"""
        name = str(quant.name)
        if name in ['Dac1','Dac2','Dac3','Dac4','Dac5','Dac6','Dac7','Dac8','Dac9','Dac10','Dac11','Dac12']:
            dacNr = (quant.name).split('Dac')
            sCmd = '{} V?\n'.format(dacNr[1])
            sAns = self.askAndLog(sCmd,bCheckError=False).strip()
            lData =  float.fromhex(sAns)
            lData = lData/838860.74-10.0
            return lData

    def performSetValue(self, quant, value, sweepRate, options={}):
        """Perform the Set Value instrument operation"""
        name = str(quant.name)
        if name in ['Dac1','Dac2','Dac3','Dac4','Dac5','Dac6','Dac7','Dac8','Dac9','Dac10','Dac11','Dac12']:
            dacNr = (quant.name).split('Dac')
            sVal = (value+10.0)*838860.74
            sCmd = '{} {}\n'.format(dacNr[1], hex(int(sVal))[2:])
            sAns = self.askAndLog(sCmd,bCheckError=False)
            if int(sAns) != 0:
              self.log('Bad response from LNHR II DAC! Set channel {} responded with error code: {}'.format(dacNr[1],sAns),level=30)
            return value
