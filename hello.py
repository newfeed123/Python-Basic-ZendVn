print("Hello 2024 python django rest framework")

x = 1
y = "hello"

print(x)
print(y)
#mặc định sep = " " và end = "\n"
print(x, y, sep="---", end="++\n")
print(type(x))
print(type(y))

res_str = "hello"
#2 cách lấy ký tự cuối của chuỗi
res1 = res_str[-1] #o
res2 = res_str[len(res_str) - 1] #o
print(res1, res2, sep=" = ")

#ko thể thay đổi ký tự trong chỗi bằng cách gán này
#res_str[1] = "a" 

#trích xuất chuỗi 
myStr = "hello python"
res3 = myStr
#from:to
res3 = myStr[2:] #lấy từ index = 2 đến cuối chuỗi
print(res3)
res3 = myStr[:2] #lấy từ index = 0 đến index = 2-1 = 1
print(res3)
res3 = myStr[2:5] #lấy từ index = 2 đến index = 5-1 = 4
print(res3)

#lấy theo bước nhảy
res3 = myStr[::2] #bước nhảy là 2
print(res3)

#đảo ngược chuỗi
res3 = myStr[::-1]
print(res3)

x = "abc"
y = "xyz"
#in ra xyc abz
xNew = y[:len(y)-1] + x[-1]
yNew = x[:len(x)-1] + y[-1]
result = xNew + " " + yNew
print(result)
