def getdate():
    import datetime
    return datetime.datetime.now()

def client_log():
    print("Enter client id to choose the client :")
    """enter 1 for harry
       enter 2 for rohan
       enter 3 for hammond
    """
    client_id=int(input("Enter id:"))
    if client_id==1:
        while True:
            with open("harryfoodlog.txt",'a') as f:
                print('Enter q to quit')
                food_log=input("Enter the food eaten :")
                
                if food_log=='q':
                    break
                else:
                    f.write(str(getdate()) +":" + " " +food_log+"\n")
                f.close()
        while True:    
            with open("harryexcerciselog.txt","a") as f:
                excersize_log=input('Enter the excersize done :')
                
                if excersize_log=='q':
                    break
                else:
                    f.write(str(getdate())+":"+" "+excersize_log +"\n")
                    f.close()

    elif client_id==2:
        while True:
            with open("Rohanfoodlog.txt",'a') as f:
                print('Enter q to skip')
                food_log=input("Enter the food eaten :")
                
                if food_log=='q':
                    break
                else:
                    f.write(str(getdate())+":"+" "+food_log +"\n")
                    f.close()
        while True:            
            with open("Rohanexcerciselog.txt","a") as f:
                excersize_log=input('Enter the excersize done :')
                if excersize_log=='q':
                    break
                else:
                    f.write(str(getdate())+":"+" "+excersize_log+"\n")
                    f.close()
    elif client_id==3:
        while True:
            with open("hammadfoodlog.txt",'a') as f:
                print('Enter q to skip')
                food_log=input("Enter the food eaten :")
                
                if food_log=='q':
                    break
                else:           
                    f.write(str(getdate())+":"+" "+food_log +"\n")
                    f.close()
        while True:        
            with open("hammadexcerciselog.txt","a") as f:
                excersize_log=input('Enter the excersize done :')
                if excersize_log=='q':
                    break
                else:
                    f.write(str(getdate())+":"+" "+excersize_log + "\n")
                    f.close()


def retrieval_log():
    
        print("Enter the client id whose log you need!")
        clientid=int(input("Enter the client id"))
        log_type=input("Enter log type for the client :")

        if clientid==1:
            if log_type=='food':
                with open("harryfoodlog.txt","r") as f:
                    print(f.readlines())
            elif log_type=='excersice':
                with open("harryexcerciselog.txt","r") as f:
                    print(f.readlines())

        if clientid==2:
            if log_type=='food':
                with open("Rohanfoodlog.txt","r") as f:
                    print(f.readlines())
            elif log_type=='excersice':
                with open("Rohanexcerciselog.txt","r") as f:
                    print(f.readlines())
        if clientid==3:
            if log_type=='food':
                with open("hammadfoodlog.txt","r") as f:
                    print(f.readlines())
            elif log_type=='excersice':
                with open("hammadexcerciselog.txt","r") as f:
                    print(f.readlines())
            



    
    
client_log()
retrieval_log()
