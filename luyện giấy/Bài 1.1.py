
danh_sach = []
for i in range(5):
    ten = input(f"Nhập tên người thứ {i+1}: ")
    danh_sach.append(ten)
print("Danh sách ban đầu:", danh_sach)


if len(danh_sach) >= 2:
    danh_sach.pop(1)
print("Danh sách sau khi xóa người thứ hai:", danh_sach)