tc=int(input("Enter Total Number Of Classes : "))
ac=int(input("Enter Attended Number Of Classes : "))

per=ac/tc*100

if per > 75:
    print("\nYou Are Eligible For The Exam...")
    
else :
    print("\nYou Are NOT Eligible For The Exam...")
    
print(f"\nYour Attendce Is {per} ")