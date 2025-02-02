users = [[1, "U1"], [7, "Rf2"], [0, "GT5"]]
# names = [item[1] for item in users]
names = list(map(lambda user: users[0], users))
print(names)
