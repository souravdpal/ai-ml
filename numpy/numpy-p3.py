#!usr/bin/python3

#importing the lib

import numpy as np

#we will revise some properties of numpy
#like shape , size , dimenisons , data types 


myArray =  np.array([[1,2,3,4,5],[6,7,8,9,10]])

#shape

shape = myArray.shape
#Dimensions
Dim = myArray.ndim
#size 
size = myArray.size
#data type
Type = myArray.dtype  


print(f"My array with Dimensions {Dim} and shape : {shape} and size {size} with data type of  {Type}")






