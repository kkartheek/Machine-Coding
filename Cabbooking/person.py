from random import randint

class Person:
    def __init__(self,name):
        self.name = name
        self.uid = name+str(randint(10,99))
