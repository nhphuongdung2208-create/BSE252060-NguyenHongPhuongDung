strings = [input(f"Nhập chuỗi {i+1}: ") for i in range(5)]

n = len(strings)
for i in range(n-1):
    for j in range(n-1-i):
        if len(strings[j]) < len(strings[j+1]):
            strings[j], strings[j+1] = strings[j+1], strings[j]
        print(strings)  # In từng bước

print("Kết quả cuối:", strings)