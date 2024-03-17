def reverse_ascending(items):
    if not items:
        return

    current_subseq = [items[0]]
    for i in range(1, len(items)):
        if items[i] > items[i - 1]:
            current_subseq.append(items[i])
        else:
            yield from reversed(current_subseq)
            current_subseq = [items[i]]
    yield from reversed(current_subseq)

# example
print(list(reverse_ascending([1, 2, 3, 4, 5])))
print(list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])))
print(list(reverse_ascending(([5, 4, 3, 2, 1]))))
print(list(reverse_ascending([])))