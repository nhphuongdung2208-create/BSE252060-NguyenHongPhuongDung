
danh_sach = ["Nguyễn", "Hồng", "Phương", "Dung", "Cute"]


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

target = input("Nhập chuỗi bạn muốn tìm: ")

result = binary_search(danh_sach, target)

if result != -1:
    print(f"Tìm thấy '{target}' tại vị trí index: {result}")
else:
    print(f"Không tìm thấy chuỗi '{target}' trong danh sách.")