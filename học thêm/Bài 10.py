#Biểu đồ cột
import matplotlib.pyplot as plt
years = [2000, 2001, 2002, 2003, 2004, 2005]
yield_data = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]

plt.plot(years, yield_data)#plot:đường, bar:cột, pie:tròn
plt.title('sản lượng theo hàng năm')
plt.xlabel('Năm')#cột x
plt.ylabel('Sản lượng (tấn trên héc ta)')#cột y
plt.show()