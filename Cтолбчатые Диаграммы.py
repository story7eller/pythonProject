import numpy as np
import matplotlib.pyplot as plt
objects = ('A', 'B', 'C', 'D', 'E', 'F')
y_pos = np.arange(len(objects))
performance = [10, 8, 6, 4, 2, 1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Value')
plt.title('Bar title')

plt.show()
