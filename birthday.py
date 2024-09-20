from datetime import datetime

currentYear = datetime.now().year
print(currentYear)
name = input("nhập vào tên của bạn: ")
birthday = int(input("Nhập vào năm sinh của bạn: "))
res = "Xin Chào {name}, năm nay bạn {age} tuổi".format(name=name, age=currentYear-birthday)
print(res)