import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

#设置标题及坐标标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

#设置标记刻度的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()