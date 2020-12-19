import matplotlib.pyplot as plt
from random_walk import  RandomWalk

while True:
    #创建一个随机漫步实例
    rw = RandomWalk()
    rw.fill_walk()

    plt.figure(figsize=(10,6))

    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,s=1)

    plt.scatter(0,0,c='green',s=5)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=5)

    #隐藏横纵坐标
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("make another walk?(y/n):")
    if keep_running == 'n':
        break