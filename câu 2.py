print ("nhập các sô lẻ từ 17 đên 111")
for i in range(111, 16, -1):
    if i % 2 == 1:
        print(i, end="")
print("/n")
else:
    la_so_nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
