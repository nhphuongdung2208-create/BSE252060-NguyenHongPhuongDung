n = int(input("Nhập n:"))
#Hình 1:
for i in range(n+1):
    print(" *" *i)

#Hình 2:
for i in range(1, n + 1):
    print(" *" *i)

#Hình 3:
for i in range(n, 0, -1):
    print(" *" *i)

# Hình 4:
for i in range(n):
    print("  " * i + "* " * (n - i))

# Hình 5:
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

# Hình 6:
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 7:
for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 8:
for i in range(n):
    for j in range(n - i):
        if i == 0 or j == 0 or j == (n - i - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 9:
for i in range(n):
    for j in range(n):
        if i == 0 or j == n - 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 10:
for i in range(n):
    for j in range(n):
        if i == n - 1 or j == n - 1 or j == (n - 1 - i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
