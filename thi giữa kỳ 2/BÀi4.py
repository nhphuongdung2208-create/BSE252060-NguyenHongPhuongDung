def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

try:
    so = int(input("Nhập một số nguyên dương: "))
    if so < 0:
        print("Vui lòng nhập số không âm.")
    else:
        print(f"Giai thừa của {so} là: {giai_thua(so)}")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên.")