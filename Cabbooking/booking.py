from random import randint
from driver import Driver

class Booking:
    def __init__(self,driver,time,src,dest,fare):
        self.driver = driver
        self.time = time
        self.src = src
        self.dest =dest
        self.fare = fare
        self.rideid = randint(100,999)

    def __str__(self):
        strret = f"Ride id{self.rideid} Driver Name {self.driver.getName()} src {self.src}" + \
                 f" dest {self.dest} fare {self.fare} "
        return strret

    def getDriver(self):
        return self.driver

    def getPosition(self):
        return self.dest