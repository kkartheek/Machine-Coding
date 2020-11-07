import datetime
import random
import vehical
import vhipass
class Processes:
    def __init__(self):
        self.toll = {}
        self.tollPrice = {}

    def add_Toll(self,name):
        if name in self.toll.keys():
            print("Name already present")
        else :
            self.toll[name] = {}

    def checkVehicalPass(self,v_no,tollName):
        #check if toll exists
        if tollName in self.toll.keys():
            #check if car is in DB
            if v_no in self.toll[tollName].keys():
                vpass = self.toll[tollName][v_no]
                cdate = datetime.datetime.now()
                delta = vpass.date - cdate
                if delta.days > 3 :
                    #pass had expired
                    return None
                elif delta.days <= 3 and vpass.type ==3:
                    return vpass
                elif delta.days <= 1 and vpass.type ==1:
                    return vpass
                else:
                    return None
            else :
                return None
        else:
            return None

    def assignCostToVehical(self,tollname,vtype):
        if vtype == 2:
            self.tollPrice[tollname][vtype] = random.randint(20, 50)
        elif vtype == 4:
            self.tollPrice[tollname][vtype] = random.randint(100, 300)

    def getTollCost(self,tollname,vtype):
        if tollname in self.tollPrice.keys():
            if vtype not in self.tollPrice[tollname].keys():
                self.tollPrice[tollname] = {}
                self.assignCostToVehical(tollname,vtype)
                return self.tollPrice[tollname][vtype]
            else :
                return self.tollPrice[tollname][vtype]
        else :
            self.tollPrice[tollname] = {}
            self.assignCostToVehical(tollname, vtype)
            return self.tollPrice[tollname][vtype]

    def checkToll(self,tollname):
        if tollname not in self.toll.keys():
            self.toll[tollname] = {}
            self.tollPrice[tollname] = {}


    def checkPass(self,tollname,vno,vtype):
        self.checkToll(tollname)
        vpass =  self.checkVehicalPass(vno,tollname)
        if vpass != None:
            return vpass
        else :
            print("No valid pass present ")
            ptype = -1
            validtype =  (0,1,2)
            while ptype not in validtype:
                ptype = int(input("Enter \n0 for oneway pass\n 1: one day pass \n 2: three day pass\n "))

            v = vehical.Vehical(vno,vtype)
            vcost = self.getTollCost(tollname,vtype)
            if ptype ==1:
                vcost = 0.8*vcost*2
            elif ptype == 2:
                vcost = 0.7*vcost*3
            if ptype !=2 :
                vpass = vhipass.Pass(v,datetime.datetime.now(),ptype,tollname)
            else:
                vpass = vhipass.Pass(v,datetime.datetime.now(),3,tollname)

            self.toll[tollname][vno]=vpass
            return vpass








