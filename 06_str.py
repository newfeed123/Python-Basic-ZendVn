class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: {name} - Age: {age}".format(name = self.name, age = self.age)
    
x = Student(name="hailan", age=18)
print(x) #goi -> fnc __str__

listCourses = [
    {'name': 'PHP', 'time': 12, 'price': 20},
    {'name': 'Django', 'time': 24, 'price': 40},
]

class Course():
    def __init__(self, name, time, price):
        self.name = name
        self.time = time
        self.price = price
    
    def showInfo(self):
        print("Name: {name} - time: {time} - price: {price}".format(
            name = self.name,
            time = self.time,
            price = self.price
        ))
    def __str__(self):
        return "Name: {name} - time: {time} - price: {price}".format(
            name = self.name,
            time = self.time,
            price = self.price
        )


result = []
for course in listCourses:
    result.append(Course(course['name'], course['time'], course['price']))

for courseObj in result:
    courseObj.showInfo()
    print(courseObj)
