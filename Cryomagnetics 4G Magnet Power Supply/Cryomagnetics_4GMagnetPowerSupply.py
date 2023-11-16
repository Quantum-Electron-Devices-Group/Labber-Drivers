#!/usr/bin/env python

from VISA_Driver import VISA_Driver
import re

__version__ = "0.0.1"

class Error(Exception):
    pass

class Driver(VISA_Driver):
    """ This class implements the Magnet Power Supply driver"""

    def performGetValue(self, quant, options={}):
        """Perform the get value operation"""
        if quant.name == 'Upper Limit':
            raw_response = self.askAndLog(quant.get_cmd)
            value, space = re.split('[A-Za-z]+',raw_response)
        elif quant.name == 'Lower Limit':
            raw_response = self.askAndLog(quant.get_cmd)
            value, space = re.split('[A-Za-z]+',raw_response)
        elif quant.name == 'Magnet Current':
            raw_response = self.askAndLog(quant.get_cmd)
            value, space = re.split('[A-Za-z]+',raw_response)
        else:
            value = self.askAndLog(quant.get_cmd)
        return value

if __name__ == '__main__':
    Driver.performGetValue()
