import array

val = array.array('i',[1,2,3,4,5,6])
print(val)

#Traversing an array

for i in range(0,6):   #Either via range or enhanced loop(Directly on iterable)
    print(val[i], end=" ") #end used as delimiter instead of new line
    