"""
Here we learn adding and removing data and matrix methods 
"""

#matrix addition

import numpy as np 

arr1 = np.arange(6)
arr2 = np.array([6,7,8,9,10])

print("matrix addition", np.concatenate((arr1,arr2))) #[0=>10] addtion

#shape of array becuse it let use know if shaped of array is same so we can perform work on it

print(arr1.shape==arr2.shape) #flase



#adding arrays inside a big array and data mod

big_Array = np.array([[1,2,3,4,5],
             [6,7,8,9,0],
             [11,12,13,15,22]])

print(big_Array.shape)

new_array_row = np.array([[12,17,18,19,20]])

new_row = np.vstack((big_Array,new_array_row))
print(new_row) 
print(new_row.shape)

print('---------------------------------------------------------------------------------------------------------')
#now adding by coloumn
column_add = np.array([1,2,3]).reshape((3,1))
new_column=np.hstack((big_Array,column_add))
print(new_column)
print(new_column.shape)


'--------------------------------------------------------------------------------'


#array deltion how arrays are delted and elemnts are deleted

new_og_array = np.array([1,2,3,4,8,5,6,7,8,9])


#if we want to delte  8 of starting becuse its making array on sorted we will 

delted_arr = np.delete(new_og_array,4)
print("after delete array" , delted_arr)


