from metricTypes import Weight,Height,HeartRate,Calories,CaloriesBurnt
from datetime import datetime
from random import randint

class Device:

    def __init__(self,type,*args):
        self.type = type
        self.devid  = type+str(randint(1000,9999))
        self.metricProperty = tuple(args)
        self.readings = []
        self.acti= {} # time data

    def getDevid(self):
        return self.devid

    def getType(self):
        return self.type

    def getDeviceSupportedMetrics(self):
        return self.metricProperty

    def addReading(self,time,*args):
        #validate the number of args
        if len(args)== len(self.metricProperty):
            self.readings.append(time,args)
            return True
        else:
            print("Missing device Metric property")
            return False

    def getMetricUnderTime(self,days):
        tmplis = []
        for reading in self.readings:
            rdays = reading[0]
            cdate = datetime.date.today()

            if (cdate-rdays) <=days :
                tmplis.append(*reading[1])

        return tmplis
typess = ["min","max"]
for type
def type(argtype)
if t