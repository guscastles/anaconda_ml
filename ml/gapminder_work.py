# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import numpy as np

ds = np.DataSource("data.txt")

data = np.array([[1, 2, 3, 4, 5, 6], [10, 7, 10, 10, 8, 20]])

pearson = np.corrcoef(data)

pearson[0, 1]

#%%
import matplotlib.pyplot as plt
from gapminder import gapminder

bics_and_us = gapminder['country'].isin(['Brazil', 'India', 'United States', 'South Africa', 'China'])

colour = {'Brazil': 'green',
         'India': 'orange',
         'United States': 'blue',
         'South Africa': 'black',
         'China': 'red'}

gapminder['colour'] = gapminder['country'].map(colour)

data = gapminder[bics_and_us]
pop = data['pop']/1e+6
year = data['year']

plt.scatter(year, pop, marker="o", s=pop/2, c=data['colour'].values)
plt.xlabel('Year')
plt.ylabel('Population in millions')
plt.title('Population Growth in BICS + US')
plt.grid(True)
plt.yticks([i*100 for i in range(15)])
plt.show()

def growth_perc(data, country):
    max_ = data['country'].max()
    min_ = data['country'].min()
    return (max_ - min_)/min_