n = int(input("Nhập n:"))
#Hình 1:
for i in range(n):
    print(" 1" *n)

# Hình 2:
for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()

# Hình 3:
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Hình 4:
for i in range(1, n + 1):
    print("  " * (i - 1), end="") # Tạo khoảng trống
    for j in range(i, n + 1):
        print(j, end=" ")
    print()

# Hình 5:
for i in range(1, n + 1):
    print("  " * (i - 1) + str(i))

#Hình 6:
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Hình 7:
for i in range(1, n):
    print(" " * (n - i), end="")
    print((str(i) + " ") * i)

# Hình 8:
for i in range(1, 5):
    print(" " * (4 - i) * 2, end="")
    for j in range(1, i + 1):
        print(j, end=" ")

# Hình 9:
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) * 2, end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

