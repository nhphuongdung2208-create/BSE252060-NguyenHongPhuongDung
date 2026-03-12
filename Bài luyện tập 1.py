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
    print(i)

#Bài 5:



