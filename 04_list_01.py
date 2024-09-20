myList = ["a", "b", "c", 1, 2, 3, ["d", "e"]]
print(myList)
print(len(myList))
print("a" in myList)
print("a" not in myList)
print(myList[-1])
print(myList[6][1])
print(myList[2:])
print(myList[:2])

myList[0] = "tada"

del myList[0]

myList.append("Python")
myList.append(["x", "y"])
myList.extend(["xx", "yy"])
print(myList)

#pop lấy ra và xóa luôn khỏi List
print(myList.pop(2))
print("myList sau khi pop", myList)

#reverse, sort, count, min, max