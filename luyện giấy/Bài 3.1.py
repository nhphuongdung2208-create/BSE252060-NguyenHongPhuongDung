
data = [
    ("Book 1", 30000),
    ("Book 2", 50000),
    ("Book 3", 100000)
]
tong = sum(item[1] for item in data)

with open("ketqua.txt", "w", encoding="utf-8") as f:
    for ten, gia in data:
        f.write(f"{ten};{gia}\n")
    f.write(f"Tong;{tong}")

print("Đã tạo file ketqua.txt thành công.")