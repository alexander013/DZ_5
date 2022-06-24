from functions import number_pi
import math

# вывод значения math.pi
print(number_pi())

# проверка правильности работы функции
k = number_pi()
if k == math.pi:
    print(True)
else:
    print(False)