# is a bad practice use global variables
sal = "HEllo global"


def salutation():
    global sal
    sal = "Hello World"
    print(sal)


def salutation2():
    sal = "Hello Everyone"
    print(sal)


salutation()
print(sal)
