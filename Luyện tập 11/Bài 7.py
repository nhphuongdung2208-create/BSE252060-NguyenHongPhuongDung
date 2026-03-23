import csv

name = input("Nhập tên nhân viên: ")
age = input("Nhập tuổi: ")
id = input("Nhập ID: ")

with open("employee.txt", "w", encoding="utf-8") as f:
    f.write(f"Name: {name}\nAge: {age}\nID: {id}\n")

with open("employee.csv", "w", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(["Name", "Age", "ID"])
    write.writerow([name, age, id])

print("Đã lưu thông tin vào employee.txt và employee.csv")

