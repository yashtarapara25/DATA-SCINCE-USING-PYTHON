pepole=int(input("How Many People Stay In Hotel :"))
day=int(input("How Many Days Stay In Hotel : "))
dis=0
print("\nWELCOME TO YT HOTEL")
rate=1000
print(f"\nPer People Rate Is {rate} For One Day....")
dis=0

if day >= 7:
    dis=rate*20/100
    print(f"\n\nCongretulation You Got {dis} Discount  Per Person")
elif day >= 3:
    dis=rate*10/100
    print(f"\n\nCongretulation You Got {dis} Discount  Per Person")
else :
     print("\nNO Discount")
     

pay=rate-dis
print(f"Per Person Pay Only {pay} Rupees..")


print(f"\n\nTotal Pay {pepole*pay} Ruppes For Stay")
      