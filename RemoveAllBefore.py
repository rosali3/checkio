# Not all of the elements are important. What you need to do here is to remove from the sequence all of the elements before the given one.

# example

# For the illustration we have a sequence [1, 2, 3, 4, 5] and we need to remove all elements that go before 3 - which are 1 and 2.

# We have two edge cases here: (1) if a cutting element cannot be found, then the sequence shoudn't be changed. (2) if the sequence is empty, then it should remain empty.

# Input: List and the border element.

# Output: List or another Iterable (tuple, iterator, generator).


from collections.abc import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    no_border_at_all_list = []
    
    for i in range(len(items)):
        if (items[i] == border):
            return items[i:]
            
        else:
            no_border_at_all_list.append(items[i])
    return no_border_at_all_list



print("Example:")
print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

# These "asserts" are used for self-checking
assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_before([], 0)) == []
assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
