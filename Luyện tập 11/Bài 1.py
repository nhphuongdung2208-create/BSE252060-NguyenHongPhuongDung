strings = [input(f"Nhập chuỗi {i+1}: ") for i in range(5)]
for i in range(1, len(strings)):
    key = strings[i]
    j = i - 1
    while j >= 0 and len(strings[j]) < len(key):
        strings[j+1] = strings[j]
        j -= 1
    strings[j+1] = key
    print(f"Bước {i}: {strings}")
print("kết quả cuối:", strings )