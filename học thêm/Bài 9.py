#nhập kí tự cách nhau bằng dấu cách
n = input("Nhập các phần tử cách nhau bởi dấu cách:").split()
n = [int(x) for x in n]
tong=0
for i in n:
    if i%3==0 or i%5==0:
        tong=tong+1
print("số phẩn tử chia hết cho 3 hoặc cho 5 là: ",tong)




