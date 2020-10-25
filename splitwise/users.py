import copy
class User:
    def __init__(self,name):
        self.expense_track_get = {}
        self.expense_track_give = {}
        self.name=name

    def display_expense(self):
        print("amount lent")
        for i in self.expense_track_get.keys():
            print(f"{i} : {self.expense_track_get[i]}")
        print("Amount borrowed")
        for i in self.expense_track_give.keys():
            print(f"{i} : {self.expense_track_give[i]}")

    def add_expense(self,dic):

        for i in dic.keys():
            if i in self.expense_track_get.keys():
                self.expense_track_get[i] += dic[i]
            else :
                self.expense_track_get[i] = dic[i]
    def update_expense_give(self,name,amount,reset=False):

        if amount==0:
            if name in self.expense_track_give.keys():
                del self.expense_track_give[name]
            return
        if name in self.expense_track_give.keys():
            if reset :
                self.expense_track_give[name] = amount
            else :
                self.expense_track_give[name] +=amount
        else :
            self.expense_track_give[name] = amount

    def update_expense_get(self,name,amt,reset=False):
        if amt == 0:
            if name in self.expense_track_get.keys():
                del self.expense_track_get[name]
            else :
                return
        if name in self.expense_track_get.keys():
            if reset:
                self.expense_track_get[name] = amt
            else :
                self.expense_track_get[name] += amt
        else:
            self.expense_track_get[name] = amt


    def pending_amt_give(self,user):
        if user in self.expense_track_give.keys():
            return self.expense_track_give[user]
        else :
            print("User not found")
            return 0

    def balence_amt_get(self,user):
        if user in self.expense_track_get.keys():
            return self.expense_track_get[user]
        else :
            return 0

    def get_usr_name(self):
        return self.name

    def settle_expense(self,user):
        usr2 = user.get_usr_name()
        if usr2 in self.expense_track_get.keys():
            u1_get =  self.balence_amt_get(usr2)  #1250
            u2_get =  user.balence_amt_get(self.name) #2830
            u1_give = self.pending_amt_give(usr2)  #2830
            u2_give = user.pending_amt_give(self.name) #1250
            '''We always need to take the max amount. This is needed as
               we round the amount, one user might get a bit more '''
            amt_u1_to_u2 = u1_give if u1_give > u2_get else u2_get
            amt_u2_to_u1 = u2_give if u2_give > u1_get else u1_get
            pending_u1_to_u2 =  amt_u2_to_u1 - amt_u1_to_u2
            if pending_u1_to_u2 < 0 :
                print(f"payment of {abs(pending_u1_to_u2)} had been done")
                self.update_expense_give(usr2,0,True)
                self.update_expense_get(usr2,0,True)
                user.update_expense_give(self.name,0,True)
                user.update_expense_get(self.name,0,True)
            else :
                print(f"{usr2} ows {abs(pending_u1_to_u2)} to {self.name}")
                self.update_expense_give(usr2,0,True)
                self.update_expense_get(usr2,abs(pending_u1_to_u2),True)
                user.update_expense_get(self.name,0,True)
                user.update_expense_give(self.name,abs(pending_u1_to_u2),True)

        print("Transaction successfull")







class ExpenseTypeCal:
    def __init__(self,nlist,share_type,slist= {},tot_amt=0):
        self.nlist =  copy.deepcopy(nlist)
        self.share =  copy.deepcopy(slist)
        self.share_type = share_type
        self.tot_amt=tot_amt

    def calAmounts(self):
        amt = {}
        cnt = 0
        if self.share_type == "percent":
            for i in self.share:
                cnt+=i
            if cnt!=100:
                raise ValueError
            for  j,i in enumerate(self.nlist):
                amt[i] = self.tot_amt*self.share[j]/100

            return amt
        elif self.share_type == "exact":
            shares =  self.tot_amt/len(self.nlist)
            flag = False
            if self.tot_amt % len(self.nlist) != 0:
                amt[self.nlist[0]] =1
                flag = True
            for i in self.nlist:
                if flag:
                    amt[i] = float(int(shares))
                else:
                    amt[i] =  shares
            if self.tot_amt % len(self.nlist) != 0:
                amt[self.nlist[0]] +=1
            return amt
        else :
            for j,i in enumerate(self.nlist):
                amt[i] =  self.share[j]
            return amt
