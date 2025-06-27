no=int(input("Enter Number :"))
count=0
while no > 0:
    digit=no%10
    count+=1
    no=no//10

print(count)
