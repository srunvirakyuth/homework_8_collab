def index_power(numbers, n):

    # check if n is less than the length of the list    
    if n < len(numbers):

        # calculate the power of the number at index n
        result = numbers[n] ** n
        return result
    
    # return -1 if n is greater than the length of the list
    else:
        return -1