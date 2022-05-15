import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, log, e


def power(a, n):
    return(1 if n == 0
           else power(a*a, n//2) if n % 2 == 0
           else a*power(a, n - 1))


x_data = np.arange(-2, 2.01, 0.01)
n = 4
b = 0.9
eps = e**-4
m = round(log(eps) / log(b)) + 1
n = m
a = 3
y_data = np.array([])
for x in x_data:
    y = 0
    for i in range(n):
        ai = power(a, i) * x * pi
        bi = power(b, i)
        y += cos(ai)*bi
    y_data = np.append(y_data, y)


plt.grid(True)


plt.plot(x_data, y_data)


plt.show()

