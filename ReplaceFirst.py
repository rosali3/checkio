# In a given sequence the first element should become the last one. An empty sequence or with only one element should stay the same.

# example

# Input: List.

# Output: List or another Iterable (tuple, iterator, generator).


from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if len(items) < 2:
        return items
    else:
        new_items = items[1:]
        new_items.append(items[0])
    return new_items


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []