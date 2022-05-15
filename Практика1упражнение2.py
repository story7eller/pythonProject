# Постройте график функции
# y(x) = x*x - x - 6
# 0 = x*x - x - 6
# x*x = x + 6

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 1)
plt.figure(figsize=(12, 8))
plt.plot(x, x*x , x, x + 6, label =r'$y(x)$')
plt.grid = True
plt.show()
# x = 3 и -2, 
