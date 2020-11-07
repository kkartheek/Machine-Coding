import Process_tkt
if __name__ == '__main__':
   intf = Process_tkt.Processes()
   opt = -1
   vopt = (1,2,3)
   while opt!=3:

       opt = int(input("Enter \n 1: ADD toll \n2: generate pass 3:exit \n"))
       if opt not in vopt:
           continue
       if (opt==1):
           tname = input("Enter the toll name")
           intf.add_Toll(tname)
       elif(opt==2):
           inn = input("Enter Vehical no type and toll \n")
           inl = inn.split()
           if len(inl) !=3:
               continue
           vpass = intf.checkPass(inl[2],inl[0],int(inl[1]))
           print(f"Pass details id{vpass.get_id()} vehical {vpass.get_Vehical().get_vehical_no()}")
