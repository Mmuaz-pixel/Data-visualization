import numpy as np 
x = np.linspace(0,20,40) # creates evenly spaced 25 numbers between 0 and 10 
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)
# print(x)
# print(np.array([x,y]).reshape(25,2))

from matplotlib import pyplot as plt

# pylab is deprecated and no longer used.

# subplot is like dividing the total graph into number of graphs
plt.subplot(2,2,1) #(rwo, column, index)

plt.plot (x,y1,'r') # r is red 
plt.subplot(2,2,2)
plt.plot (x,y2,'g--')  #dashed line
plt.subplot(2,2,3)
plt.plot (x,y3,'b*-')  #another line style 
plt.subplot(2,2,4)
plt.plot (x,y4,'o') 

# multiple plots in one graph 
# plt.plot(y,x, 'g') # g for green 
# plt.plot([0,1,2,3,4,5,6], [10,20,30,40,50,60,70])
# 

fig = plt.figure() # figure is a window in which graphs are made 

# axes are similar to subplots 
axes = fig.add_axes([0.1, 0.1, 0.5, 0.5]) # left, top, width and height of the canvas 

# By creating a figure and adding axes to it explicitly, you have more control over the layout and arrangement of your subplots within the figure. This can be useful when you want to create complex multi-plot figures or customize the position of individual subplots.

axes2 = fig.add_axes([0.5, 0.5, 0.5, 0.5])
axes2.plot(x, y2, 'g')
axes.plot(x,y1,'r')

# we can also do this 
figure3, axes__ = plt.subplots(nrows=2, ncols=2)
for ax in axes__.flatten(): # flatten is used to change a multi dimensional array into a flat array
    ax.plot(x,y1,'r')
plt.show()