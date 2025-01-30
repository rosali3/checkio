# You have a number and you need to determine which digit in this number is the biggest.

# example

# Input: A positive integer (int).

# Output: An integer 0-9 (int).


def max_digit(value: int) -> int:
    # your code here
    max_value = 0
    for item in str(value):
        if int(item) > max_value:
            max_value = int(item)
    return max_value

print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1