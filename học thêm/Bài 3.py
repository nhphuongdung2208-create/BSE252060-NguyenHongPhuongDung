#người dùng nhấn 1: yêu cầu người người dùng tính tổng 2 số a,b từ bàn phím
#người dùng nhấn 2: xuất hiện chương trình giống bài 1
#Người dùng nhấn 3: hiện ra dòng chữ "kết thúc chuong trình"


while True:
    command = input("nhập lệnh:")
    if command == "1":
        a = int(input("Nhập a:"))
        b = int(input("Nhập b:"))
        print("tổng a và b là:", a+b)
        break
    elif command == "2":
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
            break
    elif command == "3":
        print("kết thúc chương trình")
        break



