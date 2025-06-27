no=int(input("Enter Number :"))
r_no=0

while no>0:
    digit=no%10
    r_no=r_no*10+digit
    no =no //10
print(r_no)
