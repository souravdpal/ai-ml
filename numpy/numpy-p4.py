#!/usr/bin/python3

import numpy as  np

#RXC  refers  row X coloumn
#Here we will learn varios array modifaction methods

new_arr = np.arange(12) #it will arrage and make array in 0-11

#print("our orignal array : \n", new_arr)

reshaped = new_arr.reshape((3,4)) #it will make a reshaped array in given  RXC 

flat = reshaped.flatten() #it will make array again flatten in vector form 1D

ravel = reshaped.ravel() #it will also make the array in 1D but it chnages the og array insted making new in memory

transpose =  reshaped.T  #its simple RXC swap to CXR   

print("reshaped : \n" , reshaped)
print("flat 1D  : \n" , flat )
print("ravel 1D: \n " ,ravel  )
print("transpose  : \n" , transpose)


