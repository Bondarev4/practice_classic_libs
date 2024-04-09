import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


x = [25, 25, 15, 1]
my_explode = [0.5, 0, 0, 0]

plt.pie(x, labels=['a', 'b', 'c', 'd'], startangle=-90,
        explode=my_explode)
plt.show()
