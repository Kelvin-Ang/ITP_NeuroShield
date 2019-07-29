class SpiDev(object):
    def open(self,a,b):
        pass

    def close(self):
        pass

    def xfer2(self,input):
        return [0b00000000,0b00001010,0b10101010]