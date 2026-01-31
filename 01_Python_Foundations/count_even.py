def count_evens(numbers_list):
    count = 0 

    for num in numbers_list:
        if num % 2 == 0:
           count += 1 
    return count

# --- TEST ---
my_list = [1, 2, 3, 4, 5, 6]
result = count_evens(my_list)
print(f"Evens found: {result}") 
# Expected Output: Evens found: 3