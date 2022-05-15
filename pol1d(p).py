import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]

t = np.polyfit(x, y, 2)
k = np.polyfit(x, y, 1)
z = np.poly1d(k)
f = np.poly1d(t)
plt.grid(True)
plt.plot(x, y, 'o', x, f(x), 'b', x, z(x), 'r', x, y)
plt.show()


