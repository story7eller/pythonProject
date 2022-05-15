import numpy as np
import matplotlib.pyplot as plt

# равномерно распределенные значения от 0 до 5, с шагом 0.2
t = np.arange(0, 5, 0.2)

# красные черточки, синие квадраты и зеленые треугольники
plt.plot(t, t, 'r--', t, t**2,'bs', t, t**3, 'g^')
plt.show()
