def cal(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a//b

    return add,sub,mul,div

res=cal(50,10)
print("Addition : ",res[0])
print("Substraction :",res[1])
print("Multiplication :",res[2])
print("Divison :",res[3])
