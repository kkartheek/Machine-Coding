from interface import HealthTracker
if __name__ == '__main__':
    Healthapp = HealthTracker()
    op = 0
    while(op!=4):
        op = int(input("1:add user\n 2: add device \n 3:print user info 4:exit"))
        if op==1:
            user = input("Enter the user name")
            Healthapp.addUser(user)

        elif op ==2:
            uid = input("Enter the users uid")
            Healthapp.addUsersDevice(uid)
        elif op ==3:
            uid = input("Enter the users uid")
            Healthapp.printUserdev(uid)

        elif op ==4:
            uid = input("Enter the users uid")



