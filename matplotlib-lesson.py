import matplotlib.pyplot as plt
import numpy as np

fruits = ['apple', 'peach', 'orange', 'banana', 'melon']
data = [30, 40, 26, 43, 19]
bars = plt.bar(fruits, data)
bars[1].set_color('g')
plt.title('Favorite fruits')
plt.ylabel('count')

plt.show()
