import numpy as np
import matplotlib.pyplot as plt

# y(x) = x**2
# Y(x) = 2x
x = np.arange(-2.5, 2.5, 0.5)
plt.figure(figsize=(10, 5))
plt.plot(x, x**2, x, 2*x, label=r'$y(x)$')
plt.grid = True
plt.show()
