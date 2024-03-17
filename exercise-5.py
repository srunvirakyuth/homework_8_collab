def reverse_ascending(items):
    # return nothing if the list is empty
    if not items:
        return []

    # create a list to store the reversed subsequence
    current_subseq = [items[0]]

    # iterate through the list and check if the current item is greater than the previous item
    for i in range(1, len(items)):
        if items[i] > items[i - 1]:

            # append the current item to the current subsequence
            current_subseq.append(items[i])
        
        # if the current item is less than the previous item, yield the reversed subsequence
        else:
            yield from reversed(current_subseq)
            current_subseq = [items[i]]
    
    # yield the reversed subsequence
    yield from reversed(current_subseq)

# example
print(list(reverse_ascending([1, 2, 3, 4, 5])))
print(list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])))
print(list(reverse_ascending(([5, 4, 3, 2, 1]))))
print(list(reverse_ascending([])))