myList = ['x', 'y', 'z']
n = 2
res = []
for item in myList:
    index = 1
    for index in range(1, n + 1):
        ele = "{}{}".format(item, index)
        res.append(ele)
print(res)

for i in range(1, 10):
    print(i)

#pythonic style
res2 = ["{}{}".format(elm, index) for elm in myList for index in range(1, n+1)]
print(res2)

myString = 'google.com'
res3 = {}
for n in myString:
    keys = res3.keys()
    print(keys)
    if n in keys:
        res3[n] += 1
    else:
        res3[n] = 1
print(res3)

myList2 = ["PHP", "exercises", "backend"]
res4 = ""
count = 0
for ele in myList2:
    if len(ele) > count:
        count = len(ele)
        res4 = ele
print(res4)

res5 = max(myList2, key = len)
print(res5)