income=int(input("Enter Year Income :"))
tax=0
    
if income >1000000:
    tax=income*30/100
elif income  >500000 and income  >=1000000:
    tax=income*20/100
elif income >250000 and income >=500000:
    tax=income*5/100
else:
    print("No Tax........")
    

totincome=income-tax    
print("Tax =",tax)
print("Total Income :",totincome)