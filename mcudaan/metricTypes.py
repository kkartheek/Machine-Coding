from metric import Metric

# to keep simple all the metric types are kept in same file

class Weight(Metric):
    def __init__(self,value):
        super().__init__("Weight",value)
        self.unit = "kgs"

    def getValue(self):
        return self.value

    def getType(self):
        return self.type


class Height(Metric):
    def __init__(self,value):
        super().__init__("Height",value)
        self.unit = "cm"

    def getValue(self):
        return self.value

    def getType(self):
        return self.type

class HeartRate(Metric):
    def __init__(self,value):
        super().__init__("HeartRate",value)
        self.unit = "bps"

    def getValue(self):
        return self.value

    def getType(self):
        return self.type

class Calories(Metric):
    def __init__(self,value):
        super().__init__("Calories",value)
        self.unit = "kcal"

    def getValue(self):
        return self.value

    def getType(self):
        return self.type

class CaloriesBurnt(Metric):
    def __init__(self,value):
        super().__init__("CaloriesBurnt",value)
        self.unit = "kcal/h"

    def getValue(self):
        return self.value

    def getType(self):
        return self.type