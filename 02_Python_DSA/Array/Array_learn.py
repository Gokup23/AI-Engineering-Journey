array = [2,3,55,64,34,21]

#Look-up/Access
#accessed by index in constant time O(1) 
first_element = array[0]

#push/Pop - O(1) as end known
#pushing - pushing or adding element to end of array
#pop - removing an element from end of array
array.append(87)

#In some special cases when array is full , as its dynamic , python has to copy the 
#to a new place and usually double its size to fit new , therefore may require O(n) but averaged ~ O(1) safely

array.pop()
print(array)

#Insert - O(n)
'''
Insert op inserts at begining of array, or at specified loc
elements to right have to be updated with correct index as they all have shifted by one place
requiring looping thus the complexity
'''
array.insert(0,33) #at begining , shifts other elements to right by 1 
array.insert(4,0)
print(array)

#Delete - O(n)
'''
Deletes an element from a specified location in O(n)
elements to right of deleted element have to be shifted one space left , requiring looping 
'''
array.remove(55)#removes first occurence of 55
del array[2:4]#delets from index 2 - 4
print(array)

#Arrays are prefefined in python , but we will implement our own arrays

class my_array():
    def __init__(self):
        self.length = 0 #initializing length to 0
        self.data= {} #data in empty dict 
        

#Attributes of array class are stored in dictinoary by default ,
#when __dict__ method called on an instance of class it returns attributes of class along with their values in a dict format
#but when we print an array , we get elements as output, when we print instance of class
#built in __str__ called- we may modify how we need the output  

    def __str__(self):
        print(self.data.values())
        return str(seld.__dict__)



