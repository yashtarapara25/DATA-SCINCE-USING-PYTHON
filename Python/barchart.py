import matplotlib.pyplot as py
x=["c","python","ds","maths","english"]
y=[89,70,87,94,67]
c=["red","yellow","blue","green","orange"]




py.bar(x,y,
       color=c,
       edgecolor="black",
       width=0.5,
       linewidth=3,
       linestyle=":",
       alpha=0.7)






py.title("Subjects",fontsize=20)
py.xlabel("subject ",fontsize=20)
py.ylabel("mark ",fontsize=20)

py.show()
