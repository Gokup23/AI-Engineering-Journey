#################################### Array Module ####################################
# import array as arr     -     this way needs to be prefixed with arr. everytime
from array import *  # - this way can be used directly
#Aliasing - alternative names for existing Python modules or objects


val = array('i',[1,2,3,4,5,6])
print(val)

#Traversing an array

for i in range(0,6):   #Either via range or enhanced loop(Directly on iterable)
    print(val[i], end=" ") #end used as delimiter instead of new line

#Insert value in array

val.insert(2,9)  #insert(value,index)
val.append(10)  #append at end
val[2] = 7  #update or overwrite value at index 2
 
copyArray = array(val.typecode , (x*3 for x in val)) #copying array with modified values using comprehension

#Deletion:
#arr.pop(): Removes the last element (acts like a Stack).
#  # arr.pop(index): Removes the element at the specified index.
# arr.remove(value): Searches for the first occurrence of a specific value and removes it

#Searching:
#arr.index(value): Returns the index of the first occurrence of the value. Raises an error if not found.
# Slicing: arr[start:end:step]

#Taking input from user to make array
arr = array('i',[])
n = int(input('Enter  a  number (size of array) '))
for i in range(0,n):
    arr.append(int(input('Enter next value ')))
for x in arr:
    print(x,end ="")

################################### Numpy Library ####################################
from numpy import *
#float - typecasting possible
val1 = array([1,2,3,4.5] )
for x in val1:
    print(x,end=" ")

#Multideimentional arrays

zero = array(10)

one = array([1,2,3,4,5,6])

two = array([[1,2,3],[4,5,6],[7,8,9]])

three = array([ [ [1,2], [3,4]  ] , [ [5,6] , [7,8] ] ])
#Dimensions must be same to get output without error


