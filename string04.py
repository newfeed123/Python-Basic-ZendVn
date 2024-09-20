str1 = "Python is %s !!" %('easy')
str2 = "Python is %s !! Python is %s !!" %('easy', 'free')
str3 = "Course name: %s - Course price: %s"
strPython = str3 %('pythony', '10$')
strPHP = str3 %('php', 'free')
print(strPHP)

#format string
result1 = "Item one: {}".format("a")
result2 = "Item one: {} Item two: {}".format("a", "b")
result3 = "Item one: {x} Item two: {y}".format(x="a", y="b")

x = "A"
y = "B"
result4 = f'Item one: {x} Item two: 4{y}'

