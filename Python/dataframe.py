#dataframe

import pandas as pd
stud={ "name " : ["shiv","yash","rishi","siddh"],
        "r_no" : [23,45,12,56,],
       "sub"  : ["c","c++","python","ds"]}

p=pd.DataFrame(stud)
print(p)
