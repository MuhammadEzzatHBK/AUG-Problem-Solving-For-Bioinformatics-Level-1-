import matplotlib.pyplot as plt
import numpy as np

#plt.plot([1, 2, 3], [4, 5, 6])
#plt.plot([1, 2, 4, 8], [10, 20, 30, 40])
#plt.plot([2, 4, 6, 8, 10], [2, 4, 6, 8, 10])

'''
plt.plot([0.5, 1, 2, 3.5], [2, 4, 6, 8])
plt.plot([0.5, 1, 2, 3.5], [2, 4, 6, 8], 'ro')
'''

#plt.axis([0, 15, 0, 15])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

'''
# red dashes, blue squares and green triangles
t = np.arange(0., 5., 0.2) #time at 200ms intervals
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
'''

#Matplotlib Pie Plot
'''
# Data labels, sizes, and colors are defined:
labels = 'Broccoli', 'Chocolate Cake', 'Blueberries', 'Raspberries'
sizes = [30, 330, 245, 210]
colors = ['green', 'brown', 'blue', 'red']

plt.pie(sizes, labels = labels, colors = colors)
plt.axis('equal')
'''


#Matplotlib Bar Plot
'''
# Create a Line2D instance with x and y data in sequences Xdata, Ydata:
xdata=['A', 'B', 'C'] #X data
ydata=[1, 3, 5] #Y data

plt.bar(xdata, ydata)
'''

plt.show()