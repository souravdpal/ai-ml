#where conditions and indexing

'''
numpy have special operator like sql where and also we have indexing in way where we 
dont have to manually take track of index we can make index also a array to locate the 
elment in the array 
'''

import numpy as np

arr = np.array([1,2,3,4,5,5,6,5])

index = [4,5,7] #are the index of el 5 stored in this array and it can be used tracking the array and calling elments 

print("inex array print ", arr[index]) #555

 

"""
knowing indexing is important before learning how where 
work in numpy becuse when you put any condition in where it basically return
a array of index of satfiying that condition that can be used 
soon to cheq the array 
"""

condition_index = np.where(arr==5) #it will do same as index array so it will return a same array as index array
print(condition_index)
#and 
print(arr[condition_index]==arr[index]) #True True True 


#using where clause without returning the index array insted return satisfyid results 

condition_where = np.where(arr%2==0,arr ,arr+1)

print('orginal array' , arr)
print('condition where',condition_where)

"""
This is imp what happened actually here is pretty simple we get reult

result => condition where [2 2 4 4 6 6 6 6]

why? :
      where condition always in this syntax work for T/F
      np.where(condition , if (True){}, if (False){})
      like this so  when condition maths for an element and then it go to true and applies and if condition
      not able to match then it reach for false and then applied 

      so above all elements which were even where ignored becuse no condition there and which were odd get +1 becuse conditon was for even 
   Hence : we converted whole array into even array !



"""



