#!/usr/bin/env python

from VISA_Driver import VISA_Driver
import numpy as np
from time import sleep

class Driver(VISA_Driver):
    """ This class implements the Magnet Power Supply driver"""

    def performGetValue(self, quant, options={}):
        """Perform the get value operation"""
        if quant.name == 'timestats':
            try:
                raw_response = self.askAndLog(quant.get_cmd)
                mean, stddev, minval, maxval, _ = raw_response.split(",")
                result = [np.float(mean), np.float(stddev), np.float(minval), np.float(maxval)]
            except:
                n_points = 200
                freq = 277.77
                sleep(int(n_points/freq +0.5))
                try:
                    raw_response = self.askAndLog(quant.get_cmd)
                    mean, stddev, minval, maxval, _ = raw_response.split(",")
                    result = [np.float(mean), np.float(stddev), np.float(minval), np.float(maxval)]
                except:
                    result = [-1e-9, -1e-9,-1e-9, -1e-9]
            # try:
            #     mean_time=np.float(mean)
            #     standard_deviation=np.float(stddev)
            #     min_value=np.float(minval)
            #     max_value=np.float(maxval)
            #
            #     R_pre = 1e6
            #     V_off = 0.25
            #     freq = 277.77
            #     V_amplitude = 0.6
            #     duty = 0.95
            #     critical_current = 1/R_pre*(V_off+freq*V_amplitude/duty*(mean_time - 1/(freq*2)))
            # except:
            #     mean_time=-1e-9
            #     standard_deviation=-1e-9
            #     min_value=-1e-9
            #     max_value=-1e-9
            #     critical_current=-1e-9
            # self.setValue('mean_time',mean)
            # self.setValue('standard_dev',stddev)
            # self.setValue('min_val',minval)
            # self.setValue('max_val',maxval)

        return result
