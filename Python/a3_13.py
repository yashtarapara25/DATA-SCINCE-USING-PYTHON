use=int(input("Enter Elictrisity Usage : "))

if (use<=100):
    print("Rate Per Unit 5 Rupees....")
    print("Total Bill = ",use * 5)
    
elif(use<=300):
    print("Rate Per Unit 7 Rupees....")
    print("Total Bill = ",use * 7)
    
else:
    print("Rate Per Unit 10 Rupees....")
    print("Total Bill = ",use * 10)
