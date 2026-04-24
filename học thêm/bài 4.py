#Tạo dòng lệnh yêu cầu người dùng nhập mật mã
#Nếu nhập đúng sẽ hiện "đúng mk"
#nếu nhập sai: in ra "sai mật khẩu
#nhập sai 3 lần sẽ kết thức chương trình
n=1
while n<=3:
    password= input("nhap mat khau:")
    if password == "2007":
        print("Đúng mk")
        break
    else:
        print("Sai mk")
    n=n+1
print("thoat chuong trinh")



