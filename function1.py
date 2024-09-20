def showInfor1():
    print("Name: ")

def showInfor2(name = "hailan", age = 20):
    if name is None:
        name = "hailan"
    print("Name: {}, age: {}".format(name, age))

showInfor2(None, 99)

