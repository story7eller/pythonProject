import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(p)
p_f(0.5)
p_f([1, 2, 3])