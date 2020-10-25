# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import users
users_db = {}

if __name__ == '__main__':
    flag = False
    types = {'percent','exact','share'}
    while(not flag):
        print("Enter 1 to create new users\n 2 display balence \n 3 settle \n 4 add expense\n 5 exit")
        in_op = int(input("enter the option"))

        if in_op == 1:
            name = input("Enter the name ")
            if (name in users_db.keys()):
                name = input("Enter the name ")
            users_db[name]= users.User(name)
        elif in_op == 2:
            muser = input("Enter the main user")
            if muser in users_db.keys():
                users_db[muser].display_expense()
        elif in_op == 3:
            muser = input("Enter the main user")
            user1 = input("Enter the user to settle")
            if (muser not in users_db.keys()) or (user1 not in users_db.keys()):
                print("Not a valid user")
                continue
            muser_obj = users_db[muser]
            muser_obj.settle_expense(users_db[user1])

        elif in_op ==4:
            muser = input("Enter the main user")
            exp_type = input("Enter types, Allowed types Percent,exact,share")
            usr_lis = input("enter the users followed by space")
            usr_names = usr_lis.split()

            if exp_type not in types:
                raise ValueError
            totamt = float(input("Enter the value"))
            exps = []
            if exp_type != 'exact':
                for u in usr_names:
                    exps.append(float(input(f"enter the {u} portion")))
            else :
                usr_names.append(muser)
            #__init__(self,nlist,share_type,slist= {},tot_amt=0):
            amts = users.ExpenseTypeCal(usr_names,exp_type,exps,totamt)
            shares = amts.calAmounts()
            if exp_type == 'exact':
                del shares[muser]
            if muser in users_db.keys():
                muser_obj = users_db[muser]
            else :
                muser_obj = users.User(muser)
                users_db[muser] = muser_obj
            print(type(amts))
            muser_obj.add_expense(shares)
            for i in shares.keys():
                if i != muser:
                    print(i,muser)
                    if i in users_db.keys():

                        users_db[i].update_expense_give(muser,shares[i])
                    else:
                        users_db[i] =  users.User(i)
                        users_db[i].update_expense_give(muser,shares[i])


            print(shares)
        elif in_op == 5:
            flag = True








