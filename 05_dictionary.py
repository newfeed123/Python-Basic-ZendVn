myDic = {'name': 'hailan', 'age': 18}
print(myDic)
print(myDic['name'])

myDic2 = {'name': 'hailan', 'age': 18, 'score': [5, 12, 11]}
print(myDic2['score'][1])

#them phan tu vao trong dict
myDic2['name'] = 'huytran'

myDic2['address'] = {}
myDic2['address']['city'] = 'ho chi minh'
myDic2['address']['district'] = 'quan 9'
print(myDic2)