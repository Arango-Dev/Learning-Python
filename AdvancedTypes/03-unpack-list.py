numbers = [1, 2, 3]
# not eficient
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
first, *others = numbers
print(first)
