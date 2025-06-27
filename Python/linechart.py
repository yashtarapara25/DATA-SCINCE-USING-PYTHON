import matplotlib.pyplot as py
import numpy as np


arr=np.array([10,5,15,17,12,9])






py.plot(arr,
        color="red",
        linestyle=":",
        linewidth=2,
        marker="o")




py.title("Match Score ",fontsize=20)
py.xlabel("over ", fontsize=20)
py.ylabel("run ",fontsize=20)

py.show()
