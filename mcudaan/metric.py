from abc import ABC,abstractmethod

class Metric(ABC):
    def __init__(self,type,value):
        self.type= type
        self.value= value


    @abstractmethod
    def getType(self):
        pass

    @abstractmethod
    def getValue(self):
        pass