
s = " hello world"
# độ dài của chuỗi
print("độ dài của chuỗi:", len(s))
# biến chuỗi có 3 kí tự đầu thành str
a = s[0] +s[1]+s[2]
print(a)
if (a=='str'):
    print(1)
# hiện hello world hello world
print(s * 2)
# tách riêng họ với tên
a = " Nguyễn Văn A"
b = " Hoàng Thị B"
e = a.split()
f = b.split()
print(e[0])
print(f[0])
print(e[1] + ' ' + e[2])
print(f[1] + ' ' + f[2])
# đếm xem có bao nhiêu chữ số trong chuỗi
s = "I am 19 years old"
n = 0
for i in range(len(s)):
    if s[i].isdigit():
        n +=1
print(n)