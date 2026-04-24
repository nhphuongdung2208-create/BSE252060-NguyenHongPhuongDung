#tính giai thừa theo hàm đệ quy
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n-1)
n = int(input("Nhập từ bàn phím:"))
print(giai_thua(n))



