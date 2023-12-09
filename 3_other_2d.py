import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0,10,15)

fig, axes = plt.subplots(2, 3, dpi=100, figsize=(12,6))
axes[0][0].set_title("Scatter")
axes[0][0].scatter(x, x+0.2*np.random.randn(len(x))) # scatter doesn't connect

axes[0][1].set_title("Step")
axes[0][1].step(x, x**1.5) # gives a ladder shape 

axes[0][2].set_title("Bar")
axes[0][2].bar(x, x**3, align='edge', lw=1.2, width=0.5) #align = (center -default, edge, edgecenter)

axes[1][0].set_title("Fill between")
axes[1][0].fill_between(x, x**2, x**3, x**4, color='green')

data = np.random.randn(1000)
axes[1][1].set_title("Default Histogram")
axes[1][1].hist(data, color='green')

axes[1][2].set_title("Cummulative detailed Histogram")
axes[1][2].hist(data, cumulative=True, bins=10, color='green') # plotted on basis of cumulative frequency and bins specify the number of steps 

plt.show()