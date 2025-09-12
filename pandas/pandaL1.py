#importing pandas 
import pandas as pd 
import numpy as np
import math 
import random

randMarks= np.random.random(3)*math.pow(2,8)

#lets take a random data so we could able work on it 
data ={
    "user" : ["sourav" , "Shruti" ,"ruhi"],
    "marks" :[math.floor(r)for r in randMarks],
    "Majors" :["cs","Maths","AI"]
}

#first we will learn using dataframe
df = pd.DataFrame(data)

print(df)

"""
result :  
     user  marks Majors
0  sourav    100     cs
1  Shruti    206  Maths
2    ruhi     98     AI

    """



