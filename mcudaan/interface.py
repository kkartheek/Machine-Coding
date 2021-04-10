from metricTypes import Weight,Height,HeartRate,Calories,CaloriesBurnt
from device import Device
from user import User

class HealthTracker:
    _supportMetric = set()
    _healthApp = None
    def __new__(cls, *args, **kwargs):
        if HealthTracker._healthApp == None:
            HealthTracker._healthApp = super(HealthTracker, cls).__new__(cls)
            HealthTracker._supportMetric.add('Weight')
            HealthTracker._supportMetric.add('Height')
            HealthTracker._supportMetric.add('HeartRate')
            HealthTracker._supportMetric.add('Calories')
            HealthTracker._supportMetric.add('CaloriesBurnt')
        return HealthTracker._healthApp

    def __init__(self):
        self.users= {}


    def addUser(self,name):
        usr = User(name)
        uid = usr.getUid()
        self.users[uid] = usr
        print(f"Use the uid for all user related info {uid} ")

    def addUsersDevice(self,uid):
        if uid in self.users.keys():
            #valid usr
            valid_prop =""
            for prop in HealthTracker._supportMetric:
                valid_prop =valid_prop + " "+prop
            dev_prop =  input(f"Enter the set of properties,valid one {valid_prop}")
            devlis_pro =  dev_prop.split()
            dtype =input("Enter the device type")
            device = Device(dtype,devlis_pro)
            devid = device.getDevid()
            self.users[uid].addDevice(devid,device)


    def printUserdev(self,uid):
        if uid in self.users.keys():
            self.users[uid].printDevices()

    def createMetricObj(self,type,value):
        if type == "Weight":
            return Weight(type,value)
        elif type =="Height":
            return Height(type,value)
        elif type == "HeartRate":
            return HeartRate(type,value)
        elif type == "Calories":
            return Calories(type,value)
        elif type == "CaloriesBurnt":
            return CaloriesBurnt(type,value)
        else :
            return None

        

