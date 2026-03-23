lst = [1, 2, 3, 4, 5]
lst.append(int(input("Nhập phần tử cần thêm: ")))

k = int(input("Nhập giá trị k: "))
print("Số lần xuất hiện:", lst.count(k))

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

print("Tổng số nguyên tố:", sum(x for x in lst if is_prime(x)))

lst.sort()
print("Danh sách sau sắp xếp:", lst)

lst.clear()
print("Danh sách sau khi xóa:", lst)