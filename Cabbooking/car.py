from random import randint
class Car:
    def __init__(self,type,price):
        self.num = "KA"+str(randint(1000,9999))
        self.long = randint(0,100)
        self.lat = 0
        self.type = type
        self.avail = True
        self.driver = None
        self.cost = price

    def assignCarToDriver(self,driver):
        self.driver = driver

    def getDriver(self):
        return self.driver

    def getPosition(self):
        return self.long,self.lat

    def setPosition(self,long,lat):
        self.long = long
        self.lat = lat

    def getAvailability(self):
        return  self.avail

    def setAvailability(self,flag):
        self.avail= flag

    def getCabNo(self):
        return self.num

    def getCabType(self):
        return self.type

    def getCost(self):
        return self.cost



