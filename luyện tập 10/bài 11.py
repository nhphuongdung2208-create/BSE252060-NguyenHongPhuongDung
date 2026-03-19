while True:
    print("\nChọn bài tập (1-10), hoặc 0 để thoát:")
    choice = input("Nhập lựa chọn: ")

    if choice == "0":
        break
    elif choice == "1":
        path = input("Nhập đường dẫn: ")
        print("Tên file:", get_filename(path))
        print("Tên bài hát:", get_songname(path))
    elif choice == "2":
        s = input("Nhập chuỗi: ")
        ch = input("Nhập ký tự: ")
        print("Số lần xuất hiện:", s.count(ch))
    else:
        print("Lựa chọn không hợp lệ!")