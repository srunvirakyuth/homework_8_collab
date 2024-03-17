def replace_last(numbers):
    if len(numbers) > 1:

        #list.pop() removes an element from the list. Using the index -1 removes the last element
        last_number = numbers.pop(-1)

        numbers.insert(0, last_number)
        return numbers
    
    else:
        return numbers