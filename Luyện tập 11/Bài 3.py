nums = list(map(int, input("Nhập danh sách số (cách nhau bởi khoảng trắng): ").split()))
even_nums = [x for x in nums if x % 2 == 0]
print("Các số chẵn:", even_nums)
print("Tổng số chẵn:", sum(even_nums))
