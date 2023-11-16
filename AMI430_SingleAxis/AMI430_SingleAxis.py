from VISA_Driver import VISA_Driver


class Driver(VISA_Driver):
    """
    This class is an implementation of the AMI430 driver. This driver is a single axis,
    full 3D functionality is handled by the XXXX driver.

    """

    def performOpen(self, options={}):
        """
        Open connection to a AMI430 magnet power supply.
        The IP address is set when opening a connection in the Instrument Server.
        """
        VISA_Driver.performOpen(self, options)
        # Instrument will reply with "American Magnetics Model 430 IP Interface"
        # Read until term charaters (bytes=None)
        reply = self.read(n_bytes=None, ignore_termination=False)
        self.log(reply, level=20)
        # And then with "Hello"
        reply = self.read(n_bytes=None, ignore_termination=False)
        self.log(reply, level=20)

    def performClose(self, bError=False, options={}):
        """
        Close connection to instrument.
        """
        VISA_Driver.performClose(self, bError, options=options)


    def performGetValue(self, quant, options={}):

        return value

    def performSetValue(self, quant, value, sweepRate=0.0, options={}):
