def reverse_array(arr):
#using 2 pointer approach
    left = 0
    right = len(arr)-1

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        #Swapping values

        left+=1 
        right-=1
        #Moving inwards

        return arr
    
#Main code

my_data = [10,20,23,1,32,523]
print(f"Before: {my_data}")
result = reverse_array(my_data)
print(f"After: {result}")