#learning indexing and slicing of arrays 

import numpy as np 
import math 

arr = np.arange(11)
print("og array" , arr)

print("Basic slicing",arr[2:3])

#2D arrays slicing

a2D = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])
print("array 2D" , a2D)

print("We acces them using RowXcol",a2D[1,3]) #9 #rember in python and java usally arrays start from zero

print('whole row print',a2D[0]) #1,2,3,4,5
print('whole coloumn print',a2D[:,1]) #2,7

'-----------------------------------------------------------------------------------------'
#sorting and filtering of arrays 

mixArr = np.floor(9*(np.random.random(9)))

print("so its a unsorted mixed type of array",mixArr)

print("using sorted function",np.sort(mixArr))

#array filtering and array conditions
"""
just like sql we can here also have some ~same type of opertaor and syntax to make our work eassy in dealing arrays 
"""

data_nums = np.arange(11)

#we have 0-10 number we  just put conditons and make array filter or anything

#lets filter all odd number in array

odd_el = data_nums[data_nums%2!=0]
print("odd number in array are =>",odd_el)

#using a mask or say a premade codition var

condition = data_nums%2==0
print("lets print array only having elments even",data_nums[condition])


