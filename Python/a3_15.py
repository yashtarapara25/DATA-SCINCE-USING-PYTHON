product=str(input("Enter Product Name :"))
prize=int(input("Enter A Prize : "))

if (prize > 1000):
    print(f"You Get 20% Discount On  {product}.......")
    dis=prize * 20/100
    print("Discount =",dis)
    print("Total Prize =",prize - dis)
    
else:
    print(f"You Get 10% Discount On This {product}......")
    dis=prize * 10/100
    print("Discount =",dis)
    print("Total Prize =",prize - dis)
    
