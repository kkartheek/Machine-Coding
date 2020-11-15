from car import Car
from users import User
from driver import Driver
from booking import Booking
from random import randint
import math
from datetime import datetime

class TaxiBook:
    _taxiBook = None
    def __new__(cls, *args, **kwargs):
        if TaxiBook._taxiBook == None:
            TaxiBook._taxiBook = super(TaxiBook,cls).__new__(cls,*args, **kwargs)
        return TaxiBook._taxiBook

    def __init__(self):
        self.cars = set()
        self.users= {}
        self.drivers = {}
        self.type= ('hatchback','sedan','suv')
        self.costs = (10,20,30)

    def addUser(self,name):
        usr = User(name)
        print("The user id is ",usr.getUID())
        self.users[usr.getUID()] = usr

    def createCar(self):
        idx = randint(0,2)
        type = self.type[idx]
        cab = Car(type,self.costs[idx])

        self.cars.add(cab)
        return cab

    def addDriver(self,name):
        #create the car first, car and driver are decoupled. Hence you can later
        #handle the requirement of assigning the car to Driver
        cab = self.createCar()
        driver = Driver(name)

        # setting bidirectional relation
        driver.assignCab(cab)
        cab.assignCarToDriver(driver)
        print(f" Driver {name} id {driver.getDriverID()} assigned to {cab.getCabNo()} and cab type is {cab.getCabType()}")
        self.drivers[driver.getDriverID()] =  driver

    def distance(self,src1,src2):
        if len(src1)==2 and len(src2)==2:
            x1,y1 = src1
            x2,y2 = src2
            x = (x2-x1)**2
            y = (y2-y1)**2
            return int(math.sqrt(x+y))
        else :
            print("invalid Length")
            return -1


    def searchCab(self,src):
        nearCab = None
        mindis = 0
        for cab in self.cars:
            if nearCab == None and  cab.getAvailability():
                nearCab = cab
                src1 = tuple(cab.getPosition())
                mindis = self.distance(src, src1)

            if  cab.getAvailability():
                src1 = tuple(cab.getPosition())
                dis = self.distance(src,src1)
                if dis < mindis:
                    nearCab = cab

        if cab==None:
            #all cabs are busy
            return None
        else:
            return nearCab

    def bookCab(self,usrid,src,dst):
        if usrid in self.users.keys():
            cab = self.searchCab(src)
            if (cab == None):
                print("All Cabs are busy, plz try in some time")
                return None
            else :
                fare = cab.getCost()
                dis = self.distance(src,dst)
                cost = fare*dis
                now = datetime.now()

                current_time = now.strftime("%H:%M:%S")
                ride = Booking(cab.getDriver(),current_time,src,dst,cost)

                #usr params
                usr = self.users[usrid]
                usr.setPay(cost)
                usr.setBookings(ride)

                #driver info
                driver = cab.getDriver()
                driver.addRide(ride)

                cab.setAvailability(False)
                return ride

        else :
            print("Not a valid user")
            return


    def finishRide(self, usrid, ride):
        if usrid in self.users.keys():
            usr = self.users[usrid]
            driver = ride.getDriver()
            car = driver.getCab()
            car.setAvailability(True)
            long,lat = ride.getPosition()
            car.setPosition(long,lat)

    def userRides(self,usrid):
        if usrid in self.users.keys():
            usr = self.users[usrid]
            for ride in usr.getBookings():
                print(ride)

    def driverRides(self,usrid):
        if usrid in self.drivers.keys():
            driver = self.drivers[usrid]
            for ride in driver.getRides():
                print(ride)




