#Bài 1:
import matplotlib.pyplot as plt

labels = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
values = [6, 10, 12, 4, 1]

plt.bar(labels, values, color=['green','blue','orange','red','purple'])
plt.title("Kết quả học tập của lớp")
plt.xlabel("Xếp loại")
plt.ylabel("Số lượng học sinh")
plt.show()

#Bài 2:
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y1 = x**2
y2 = x**3

plt.plot(x, y1, color='blue', label='y = x^2')
plt.plot(x, y2, color='red', label='y = x^3')

plt.title("Đồ thị y = x^2 và y = x^3")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

#BÀi 3:
import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D", "E"]
sizes = [30, 25, 15, 20, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Tỷ lệ doanh số sản phẩm")
plt.show()

#Bài 4:
import matplotlib.pyplot as plt

# Ví dụ dữ liệu top 10 thành phố lớn nhất California theo diện tích (km2)
cities = ["Los Angeles", "San Diego", "San Jose", "San Francisco",
          "Fresno", "Sacramento", "Long Beach", "Oakland",
          "Bakersfield", "Anaheim"]

areas = [1302, 964, 466, 121, 296, 259, 170, 202, 382, 131]

# Sắp xếp dữ liệu giảm dần
sorted_data = sorted(zip(areas, cities), reverse=True)
areas_sorted, cities_sorted = zip(*sorted_data)

plt.barh(cities_sorted, areas_sorted, color='skyblue')
plt.xlabel("Diện tích (km²)")
plt.ylabel("Thành phố")
plt.title("Top 10 thành phố lớn nhất California theo diện tích")
plt.gca().invert_yaxis()  # Để thành phố lớn nhất ở trên cùng
plt.show()


