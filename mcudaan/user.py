from random import randint
from device import Device

class User:
    def __init__(self,name):
        self.name = name
        self.uid = name+str(randint(100,999))
        self.device = {}

    def getUid(self):
        return self.uid

    def addDevice(self,devid,device):
        self.device[devid] = device

    def getDevice(self,devid):
        pass
        #return self.device[dev]

    def delDvice(self,devid):
        del self.device[devid]

    def printDevices(self):
        for dev in self.device.keys():
            print(f"The Device is  {self.device[dev].getType()} and id {dev}")
            for metric in self.device[dev].getDeviceSupportedMetrics():
                print("\tMetric",metric)

    def addData(self,devid,time,*data):
        if devid in self.device.keys():
            self.device[devid].addReading(time,data)
        else:
            print("Invalid device")

    def getDeviceStats(self,devid,days):
        if devid in self.device.keys():
            return self.device[devid].getMetricUnderTime(days)
        else:
            print("Invalid device")
            return None
