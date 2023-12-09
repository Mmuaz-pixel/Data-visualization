import numpy as np 
import matplotlib.cm as cm
import matplotlib.pyplot as plt 

# np.arrange is used to make a array from starting pos to ending with a specified gap between values 

delta = 0.025 

x = np.arange(-3, 3, delta)
y = np.arange(-2, 2, delta)

X, Y = np.meshgrid(x,y)



# Pie chart 

languages = ['Python', 'C++', 'Javascript', 'Java']
popularity = [22, 17, 19, 8]

explode = (0.1, 0.05, 0.05, 0.05)
# explode is like how much the specific pie is away from the pie chart (stands out)
plt.pie(popularity, labels=languages, explode=explode, shadow=True, startangle=0, autopct='%1.1f%%')
plt.show() 