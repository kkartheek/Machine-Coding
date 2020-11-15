from person import Person

class User(Person):
    def __init__(self,name):
        super().__init__(name)
        self.pay = 0
        self.bookings = []

    def getName(self):
        return self.name

    def getPay(self):
        return self.pay

    def setPay(self,pay):
        self.pay+=pay

    def getBookings(self):
        return self.bookings

    def setBookings(self,trip):
        self.bookings.append(trip)

    def getUID(self):
        return self.uid

