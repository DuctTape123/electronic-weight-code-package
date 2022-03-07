import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

header = ['Port 0', 'Port 1', 'Port 2', 'Port 3']
fig, axd = plt.subplot_mosaic([['tl', 'tr'],['b', 'b']], constrained_layout = True)
ax1 = axd['b']
ax2 = axd['tl']
ax3 = axd['tr']
sumar = []
tar= []
def animate(i):
    pullData = open("C:\\Computer Science\\School project in Py\\Phidget_1046_0_Python_Example\\data.txt","r+").readline()
    dataArray = pullData.split(' ')
    ax2.clear()
    ax1.clear()
    ax3.clear()
    dataArray[0] = round((float(dataArray[0])) / 240) + 6
    dataArray[1] = round((float(dataArray[1])) / 240) + 1
    dataArray[2] = round((float(dataArray[2])) / 240) - 1
    dataArray[3] = round((float(dataArray[3])) / 240) + 5
    sum = dataArray[0] +  dataArray[1] +  dataArray[2] + dataArray[3]
    print(sum)
    sumar.append(sum)
    tar.append(i * 0.5)
    st = ax3.text(0.5, 0.5,'the total amount of weight is ' + str(sum) + 'lbs', ha = 'center', va = 'center', size =10)
    ax2.set(ylim=(0, 200), yticks= np.arange(0, 200, 20))
    ax2.bar(header, dataArray)
    ax2.set_ylabel('lbs')
    ax1.plot(tar, sumar)
    ax1.set_xlabel('seconds')
    ax1.set_ylabel('lbs')
ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()