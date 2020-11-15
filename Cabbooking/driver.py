from person import Person

class Driver(Person):
    def __init__(self,name):
        super().__init__(name)
        self.cab = None
        self.rides = []

    def assignCab(self,cab):
        self.cab = cab

    def getCab(self):
        return self.cab

    def getRides(self):
        return self.rides

    def addRide(self,ride):
        self.rides.append(ride)

    def getDriverID(self):
        return self.uid

    def getName(self):
        return self.name
