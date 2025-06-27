sub1=int(input("Enter First Subject Mark : "))
sub2=int(input("Enter Secouond Subject Mark : "))
sub3=int(input("Enter Third Subject Mark : "))

total=sub1+sub2+sub3
per=total/3

if sub1>40 and sub2>40 and sub3>40:
    print("\n\nResult = PASS")
    print("Persantage = ",per)
  
    if per >= 75:
        print("Rank = Distinction")
    elif per >=60:
        print("Rank = First Class")
    else:
         print("Rank = Secound Class")
    
else :
    print("\n\nResult = FAIL")
    print("Persantage =",per)
    print(f"Better Luck Next Time.......")
    
