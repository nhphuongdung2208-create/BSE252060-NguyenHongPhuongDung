#Tạo lớp student có tính năng (name, grade)
class student:
    def __init__(selt, name, grade):
        selt.name = name
        selt.grade = grade
@property
def name(self):
    return self.name
@property
def grade(self):
    return self.grade
@name.setter
def name(self, value):
    self.name = value
@grade.setter
def grade(self, value):
    if value < 0 or value > 100:
        raise ValueError()
    self__grade = value

def __str__(self):
    return f"{self.name} is {self.grade}"
YA = student("Dung", 9)
print(YA.name)


