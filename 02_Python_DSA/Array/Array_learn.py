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
        return str(self.__dict__)
    
    def get(self,index):
        return self.data[index] #takes index as parameter and returns corresponding value
    
    def push(self, item):
        self.length += 1 
        self.data[self.length - 1] = item #Adds item at end

    def pop(self):
        last_item = self.data[self.length-1] #collects last element
        del self.data[self.length - 1] #deletes last ele
        self.length -=1 # reduces length by 1 
        return last_item # returns popped element
    
    def insert(self,index,item):
        self.length +=1
        for i in range(self.length-1 , index,-1):
            self.data[i] = self.data[i-1] #shifts every element from index to end by 1 place towards right
            self.data[index] = item #adds element at given index , O(n) operation

    def delete(self,index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1] #Shifts elements from given index to end by one place towards left
        del self.data[self.length-1] # The last element which remains 
    # because arrays are contingious and gaps arent allowed



