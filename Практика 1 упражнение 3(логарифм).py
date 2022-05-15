import math
import numpy as np

print('log value for base 2: ')
print(math.log2(16)) #  в какую степень нужно возвести 2 ку что бы получить 16
print('log value for base 4: ')
print(math.log(16, 4)) # в какую степень нужно возвести 4рку что бы получить 16
print('Log Value for base 10: ')
print(math.log10(100))
# log1p(x) = log1p(1 + x)
print('Log value(1 + 15) for x = 15 is : ')
print(math.log1p(7))
print(math.log(16))
inp_arr = [10, 20, 30, 40, 50]
print('Array input elements:\n', inp_arr)
import numpy as np
res_arr = np.log(inp_arr)
print('Relustant array elements:\n', res_arr)
print('math.exp(-45.17 : ', math.exp(-45.17))
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.1)
z = np.sin(x)
j = np.tan(1/(1 + z**2))
k =(-(np.fabs(x)/10))
i = np.exp(k)
q = x**2 + 1
plt.plot(x, np.log1p(j)**q*i )





print('Проверяем х: ', q+1)

plt.show()

