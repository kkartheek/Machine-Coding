import random
class Pass:
    def __init__(self,vehical,date,type,toll):
        self.vehical = vehical
        self.date = date
        self.type = type
        self.id = toll+str(random.randint(100,999))
    def get_id(self):
        return self.id

    def get_date(self):
        return self.date

    def get_pass_type(self):
        return self.type

    def get_Vehical(self):
        return self.vehical

