"""
here are some more other numpy opertaion that can be helpful
"""

#vector dot product
import numpy as np 
import random

v1 = np.array([1,2,3,4,5,6])
v2 =np.array([3,7,8,9,3,2])

print(v1.size==v2.size)
print("Dot product of two vectors" , np.dot(v1,v2))



#sum

print("sum of vector or array" , np.sum(v1) , "is the sum of all elments of vector 1")

#mean value of vectore 

print("mean of  vector or array" , np.mean(v1) ,"is the mean of all elments of vector 1")


#np cumsum => cumilative sum  examples  [1,2,3] => (((0+1)+2)+3)


print("cumsum of  vector or array" , np.cumsum(v1) ,"is the cum of all elments of vector 1")


#trignometry

"""
arc cos and sin gave the angle of given value so rember the angle always will be under the domain of 
sin and cos = > [-1,1]
that's else you hit NAN 
"""

#lets make a random angle so we can get random angles form the sin and cos arc

vc1 = (np.random.random(3))
vc2 = (np.random.random(3))
dot  = np.dot(vc1,vc2)


print("cos value of dot product",np.arccos(dot))  
print("sin value of dot product " ,np.arcsin(dot))


