import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('./iris.csv')
# sns.barplot(x = 'sepal.length', y='petal.length', data=data)
# sns.lineplot(x='petal.length', y='sepal.length', data=data)
# sns.countplot(x='petal.width', data=data)
# sns.countplot(x='petal.length', hue='variety', data=data)

# data = pd.read_csv('./titanic.csv')

# sns.histplot(data['Age'], bins=16)
# sns.distplot(data['Age'], bins=16)

# for column in data.columns:
#     if not data[column].apply(lambda x: isinstance(x, (float, int))).all():
#         data = data.drop(column, axis=1)

# sns.heatmap(data.corr(), cbar=True)

# in a heat map, the darker area shows the inverse relation 

# sns.pairplot(data) # gives scatter plot for every two pairs possible 
# sns.pairplot(data, hue='variety')
# sns.lmplot(x = 'petal.length', y='sepal.length', data=data) #used in linear regression models 
sns.lmplot(x = 'petal.length', y='sepal.length', hue='variety', data=data)
print(data.head())
plt.show()