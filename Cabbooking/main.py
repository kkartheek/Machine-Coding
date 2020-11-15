from interface import TaxiBook
if __name__ == '__main__':
    taxeService = TaxiBook()
    opt = -1
    while opt !=6:
        print("1: add usr\n 2:add driver\n 3: book a ride\n 4:Display user rides\n 5: Display driver rides\n 6:Exit\n")
        opt = int(input("Enter the option"))
        if opt not in range(0,6):
            continue
        else:
            if opt==1:
                user = input("Enter the username")
                taxeService.addUser(user)
            elif opt==2:
                driverName = input("Enter the Driver name")
                taxeService.addDriver(driverName)
            elif opt==3:
                usrid = input("Enter a valid usrid")
                srcloc = input("Enter  src Logitude followed by Latitude")
                dstloc = input("Enter dst Logitude followed by Latitude")
                srct = srcloc.split()
                dstt = dstloc.split()
                if len(srct)==2 and len(dstt) ==2:
                    src = (int(srct[0]),int(srct[1]))
                    dst = (int(dstt[0]),int(dstt[1]))
                    ride = taxeService.bookCab(usrid,src,dst)
                    if ride != None:
                        taxeService.finishRide(usrid,ride)
                    else:
                        print("No cabs available")
            elif opt==4:
                usrid = input("Enter a valid usrid")
                taxeService.userRides(usrid)
            elif opt==5:
                usrid = input("Enter a valid drivers usrid")
                taxeService.driverRides(usrid)
