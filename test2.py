print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
print("Display manu \n 1.	Add a record \n 2.	Search a record \n 3.	Update a record \n 4.Sort the record alphabetically \n 5.Delete a record \n 6.Quit")
manu=int(input("Enter your choice: "))
phoneDirectory={}
y=[]
i=1
while(manu!=6):
    if(manu==1):
        x=input("Enter name: ")
        if x.isalpha() :
            print()
        else:
            print("error")

        y=(input("Enter your 10-digit phone number:"))
        if len(y)==10 and y.isnumeric():
            phoneDirectory[x]=y
            phoneDirectory.update({x:y})
            print("Record added",phoneDirectory)
        else:
            print("error")
        
    elif(manu==2):
        b=input("Enter the name that you want to search: ")
        if b in phoneDirectory:
            print(b,":",phoneDirectory[b])
        else:
            print("No name exist in phonedirectory. ") 
    elif(manu==3):
        c=input("Enter the name you want to update: ")  
        d=input("Enter your 10-digit phone number want to update: ") 
        phoneDirectory.update({c:d})  
        print(phoneDirectory)
    elif(manu==4):
        sorted_phonedirectory=dict(sorted(phoneDirectory.items()))
        print("sorted records",sorted_phonedirectory)
    elif(manu==5):
        c=input("Enter the name that you want to delete:")
        if c in phoneDirectory:
                phoneDirectory.pop(c)
                print("Record deleted")
        elif len(phoneDirectory) ==0:
            print("phonedirectory is empty,no name is found" )
        else:
            print("name not found in phonedirectory.")

        

    print("Display manu \n 1.	Add a record \n 2.	Search a record \n 3.	Update a record \n 4.Sort the record alphabetically \n 5.Delete a record \n 6.Quit")
    manu=int(input("Enter your choice: "))
else:
    print("Now,you exits from the whole program")