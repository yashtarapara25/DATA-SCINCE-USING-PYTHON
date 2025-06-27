product=input("Enter A Product Name :")
prize=int(input("Enter A Prize :"))
discount=0

if prize >=5000:
    discount=prize*30/100
elif prize >=1000:
    discount=prize*20/100
elif prize >=500:
    discount=prize*10/100
else:
    print("No Discount On This Prize.......")
    
pay=prize-discount
print(f"You Pay {discount} Less In {product}")
print("Total Prize =",pay)