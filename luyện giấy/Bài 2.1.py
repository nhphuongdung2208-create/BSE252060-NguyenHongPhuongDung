import math

def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n = int(input("Nhập số lượng phần tử: "))
mang = []
for i in range(n):
    mang.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

so_le = [x for x in mang if x % 2 != 0]
print(f"Dòng 1: Các số lẻ: {so_le} - Tổng số lượng số lẻ: {len(so_le)}")

so_nt = [x for x in mang if la_so_nguyen_to(x)]
print(f"Dòng 2: Các số nguyên tố: {so_nt}")