myList = ["node", "python", "abc"]

for item in myList:
    print(item)

myDic2 = {'name': 'hailan', 'age': 18, 'score': [5, 12, 11]}

for key in myDic2:
    # print(key+":", myDic2[key])
    if(key == "score"):
        print("key: %s - sum value: %d" %(key, sum(myDic2[key])))
    else:
        print("key: %s - value: %s" %(key, myDic2[key]))

i = 0 
while i <= 5:
    print(i)
    i = i + 1
    break