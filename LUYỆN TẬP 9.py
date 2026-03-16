#Bài 1:
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = weight / (height * height)
print("BMI của bạn là:", round(bmi, 2))

#Bài 2:
num = int(input("Nhập một số: "))
total = 0

for digit in str(num):
    total += int(digit)

print("Tổng các chữ số là:", total)

#Bài 3:
name = input("Nhập tên: ")
normalized_name = " ".join(name.strip().split())
normalized_name = normalized_name.title()

print("Tên chuẩn hóa:", normalized_name)

#bài 4:
text = input("Nhập chuỗi các kí tự từ bàn phím: ")

upper_count = sum(1 for c in text if c.isupper())
lower_count = sum(1 for c in text if c.islower())
digit_count = sum(1 for c in text if c.isdigit())
space_count = text.count(" ")
special_count = sum(1 for c in text if not c.isalnum() and not c.isspace())

print("Chữ hoa:", upper_count)
print("Chữ thường:", lower_count)
print("Chữ số:", digit_count)
print("Khoảng trắng:", space_count)
print("Ký tự đặc biệt:", special_count)

#Bài 5:
class User:
    def __init__(self, user_id):
        self._id = user_id

    @property
    def id(self):
        return self._id

u = User(22082007)
print("User ID:", u.id)

#BÀi 6:
class Product:
    def __init__(self, price):
        self._price = price

    def price(self):
        return self._price

    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Giá phải > 0")

    def __str__(self):
        return f"Product price: {self._price}"

p = Product(100)
print(p)
p.price = 200
print(p)

#Bài 7:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

p = Person.from_string("DUNG-20")
print(p.name, p.age)

#Bài 8:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)

#Bài 9:
class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    def __eq__(self, other):
        return self.diem == other.diem

#vd
sv1 = SinhVien(8.5)
sv2 = SinhVien(8.5)
sv3 = SinhVien(9.0)

print("sv1 == sv2:", sv1 == sv2)  # True
print("sv1 == sv3:", sv1 == sv3)  # False

#bài 10:
class SinhVien:
    count = 0  # biến lớp để đếm số đối tượng

    def __init__(self, diem):
        self.diem = diem
        SinhVien.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

#vd
sv1 = SinhVien(7)
sv2 = SinhVien(8)
sv3 = SinhVien(9)

print("Số lượng SinhVien được tạo:", SinhVien.get_count())

#Bài 11:
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  # gọi constructor lớp cha

    def sound(self):
        print("Gâu gâu!")  # ghi đè phương thức

#vd
dog = Dog("Nhon")
print("Tên:", dog.name)
dog.sound()





