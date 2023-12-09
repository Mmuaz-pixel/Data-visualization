import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,20, 40)
y1 = x*(x/4) + x
y = np.sin(x)

# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.3, 0.5, 0.4, 0.4])

# axes1.plot(x, y1, 'r', label="y = x*x/4 + x")
# axes2.plot(x,y, 'g', label="y=sin(x)")
# axes1.legend()
# axes2.legend() # legend functions make the labels appear 

fig, axes = plt.subplots(1,3,dpi=100)
axes[0].plot(x, x**1.1, label="y = x^1.1", linewidth=0.2)
axes[1].plot(x, x**1.2, label="y = x^1.2", linewidth=1, marker='*')
axes[2].plot(x, x**1.3, label="y = x^1.3", linewidth=1.5, marker='o', markerfacecolor='red') # places a o for each x value
for ax in axes:
    ax.legend()
    ax.grid(True)

# setting limits 

axes[0].set_ylim([0,20])
plt.show()