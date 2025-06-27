f_side=int(input("Enter First Side Of Tringle :"))
s_side=int(input("Enter Secound Side Of Tringle :"))
t_side=int(input("Enter Third Side Of Tringle :"))

if f_side+s_side>t_side and f_side+t_side>s_side and s_side+t_side>f_side:
    print("Tringle Valide")
else:
    print("Tringle Not Valide")
