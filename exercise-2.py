def index_power(numbers, n):

    # check if n is less than the length of the list    
    if n < len(numbers):

        # calculate the power of the number at index n
        result = numbers[n] ** n
        return result
    
    # return -1 if n is greater than the length of the list
    else:
        return -1
    
# Test cases
print(index_power([1, 2, 3, 4], 2)) # 9
print(index_power([1, 3, 10, 100], 3)) # 1000000
print(index_power([0, 1], 0)) # 1
print(index_power([1, 2], 3)) # -1