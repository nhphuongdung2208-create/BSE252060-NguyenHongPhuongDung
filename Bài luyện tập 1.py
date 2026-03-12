#Bài 1:
a = 10
b = 4
result = (a**2 + b**2) / (a - b)
print("Kết quả:", result)

#Bài 2:
import math

# Nhập hai số từ bàn phím
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# Lũy thừa (a^b)
power = a ** b

# Căn bậc 2 của a và b
sqrt_a = math.sqrt(a)
sqrt_b = math.sqrt(b)

# Chia lấy phần nguyên
div_int = a // b

# Chia lấy phần dư
div_mod = a % b

# Làm tròn số (round)
rounded_a = round(a)
rounded_b = round(b)


print("Lũy thừa a^b:", power)
print("Căn bậc 2 của a:", sqrt_a)
print("Căn bậc 2 của b:", sqrt_b)
print("Chia lấy phần nguyên a//b:", div_int)
print("Chia lấy phần dư a%b:", div_mod)
print("Làm tròn a:", rounded_a)
print("Làm tròn b:", rounded_b)

#Bài 3:
n = int(input("Nhập một số từ 1 đến 9: "))

if 1 <= n <= 9:
    print(f"Bảng cửu chương của {n}:")
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")
else:
    print("Số không hợp lệ! Vui lòng nhập từ 1 đến 9.")

#Bài 4:
for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i, end=" ")

#Bài 5:
import random

# Nhập số hàng và số cột
M = int(input("Nhập số hàng (M): "))
N = int(input("Nhập số cột (N): "))

# Khởi tạo ma trận M x N với phần tử ngẫu nhiên từ 1 đến 100
matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]

# Hiển thị ma trận
print("Ma trận vừa tạo:")
for row in matrix:
    print(row)

# Hiển thị một hàng bất kỳ
row_index = int(input("Nhập số thứ tự hàng muốn hiển thị (1 đến M): ")) - 1
if 0 <= row_index < M:
    print(f"Hàng {row_index+1}:", matrix[row_index])
else:
    print("Chỉ số hàng không hợp lệ!")

# Hiển thị một cột bất kỳ
col_index = int(input("Nhập số thứ tự cột muốn hiển thị (1 đến N): ")) - 1
if 0 <= col_index < N:
    print(f"Cột {col_index+1}:", [matrix[i][col_index] for i in range(M)])
else:
    print("Chỉ số cột không hợp lệ!")

# Hiển thị giá trị lớn nhất trong ma trận
max_value = max(max(row) for row in matrix)
print("Giá trị lớn nhất trong ma trận là:", max_value)

#BÀi 6:
import math
#Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi số, cách nhau bằng dấu ';': ")

# Tách chuỗi thành danh sách số nguyên
numbers = [int(x.strip()) for x in s.split(";")]

# In từng số trên một dòng
print("Các số trong chuỗi:")
for num in numbers:
    print(num)

# Đếm số chẵn
even_count = sum(1 for num in numbers if num % 2 == 0)

# Đếm số âm
negative_count = sum(1 for num in numbers if num < 0)

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Đếm số nguyên tố
prime_count = sum(1 for num in numbers if is_prime(num))

# Tính giá trị trung bình
average = sum(numbers) / len(numbers)

# In kết quả
print("Số lượng số chẵn:", even_count)
print("Số lượng số âm:", negative_count)
print("Số lượng số nguyên tố:", prime_count)
print("Giá trị trung bình:", average)

#Bài 7:
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# Khởi tạo 2 đối tượng
sv1 = Student("P", 8)
sv2 = Student("D", 9)

print(sv1.name, sv1.score)
print(sv2.name, sv2.score)

#Bài 8:
n = int(input("nhập từ 0 đến 10: "))
if 0 <= n <= 10:
    print(f"Điểm sinh viên: {n}")
else:
    print("Số không hợp lệ! Vui lòng nhập từ 0 đến 10.")

#Bài 9:
class Student:
    def __init__(self, name, score):
        if 0 <= score <= 10:
            self.name = name
            self.score = score
        else:
            raise ValueError("Điểm phải nằm trong khoảng 0–10")

    def display(self):
        print(f"Sinh viên {self.name} có điểm là {self.score}")

# VD
sv1 = Student("P", 10)
sv2 = Student("D", 7)

sv1.display()
sv2.display()


#BÀi 10:
FILE_NAME = "products.txt"

# Hàm thêm sản phẩm vào file
def add_product(code, name, price):
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{code};{name};{price}\n")

# Hàm đọc danh sách sản phẩm từ file
def read_products():
    products = []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == 3:
                code, name, price = parts
                products.append((code, name, float(price)))
    return products

# Hàm hiển thị danh sách sản phẩm
def display_products(products):
    for p in products:
        print(f"{p[0]} | {p[1]} | {p[2]}")

# Hàm sắp xếp theo giá giảm dần
def sort_by_price_desc(products):
    return sorted(products, key=lambda x: x[2], reverse=True)


# Thêm sản phẩm
add_product("sp1", "Cocacolala", 15.5)
add_product("sp2", "Bưởi 5 Roi", 18.0)
add_product("sp3", "Bia 333", 14.5)

# Đọc và hiển thị
print("Danh sách sản phẩm:")
products = read_products()
display_products(products)

# Sắp xếp theo giá giảm dần
print("\nDanh sách sản phẩm (giá giảm dần):")
sorted_products = sort_by_price_desc(products)
display_products(sorted_products)

