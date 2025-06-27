age=int(input("Enter Age : "))

print("\n\nWelcome Theme Park ")
if age > 60:
    print("Ticket Prize = 700")
elif age > 18 and age >=60:
    print("Ticket Prize = 1000")
elif age > 5 and age >=18:
    print("Ticket Prize = 500")
else :
    print("FREE......")