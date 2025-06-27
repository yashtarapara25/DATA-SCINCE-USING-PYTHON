import random

secnumber=random.randint(1,100)

print("Welcome To the Number Gussing game !!")
print("Guess a number between 1 and 100.")

while True:

    num=int(input("Guees The Number :"))

    if num<secnumber:
        print("Number Is low, Try Again ...!!\n")
    elif num>secnumber:
        print("Number Is High,Try Again ...!!\n")
    else:
        print("\nCongratiulation You Got Acchivment...!!")
        break
    
print("Thanks For Playing...")

    
