#nhập mật khẩu 5 lần
#mật khẩu là 30
#thoát chương trình nhập exit

MK = "30"
count = 0
while count < 5:
    a = input("Nhập mật khẩu: ")
    if a == MK:
        print("Đúng mật khẩu")
        break
    elif a == "exit":
        print("Thoát màn hình ")
        break
    else:
        count += 1
        print("sai mật khẩu")
if count == 5:
    print("Đã hết lượt")



