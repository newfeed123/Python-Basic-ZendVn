class People():
    def __init__(self, paramName, paramAge):
        print("People __init__")
        self.name = paramName
        self.age = paramAge
    def showInfo(self):
        print("Name: {name} - Age: {age}".format(name = self.name, age = self.age))
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
class Student():
    def __init__(self, paramName, paramAge, school):
        People.__init__(self, paramName, paramAge)
        self.school = school
        print("Student __init__")
    def showInfo(self):
        People.showInfo(self)
        print("school: {school}".format(school = self.school))
    def setShool(self, school):
        self.school = school

# x = Student(paramName="huy", paramAge=12)
# print(x.name)
# x.setAge(20)
# print(x.age)
# # print(x.school)
# print(type(x))
# x.showInfo()

# y = Student("lyn lyn", 1)
# print(y.name)
# print(y.age)
# print(y.school)

h = Student(paramName="hailen", paramAge=18, school="zendvn")
h.showInfo()
h.setShool("thdoantung")
h.showInfo()