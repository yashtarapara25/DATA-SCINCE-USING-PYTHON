import matplotlib.pyplot as py
x=[30,20,60,35,25]
y=["English","Maths","python","ds","C"]
c=["red","blue","yellow","brown","green"]
ex=[0.0,0.2,0.0,0.0,0.0]




py.pie(x,
       labels=y,
       colors=c,
       labeldistance=0.7,
       shadow='true',
       radius=0.9,
       autopct='%2.2f%%',
       explode=ex)







py.title("Result Information ")
py.show()
