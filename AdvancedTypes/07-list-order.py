numbers = [2, 8, 7, 5, 3, 6]
# numbers.sort(reverse=True)
num2 = sorted(numbers, reverse=True)
print(numbers)
print(num2)

users = [[1, "U1"], [7, "Rf2"], [0, "GT5"]]


def sortfn(element):
    return element[0]


users.sort(key=sortfn)
print(users)
