import numpy as np
from functools import reduce

temp = np.array([-11.3, -13.7, -10.8, -3.5, 5.8, 12.9, 18.1, 20.6, 19.7, 14.1, 6.3, -2.9]) # dec jan feb ...
print(max(temp))
print(min(temp))
print(temp.mean())
print(" ".join([str(temp[i * 3 : (i + 1) * 3].mean()) for i in range(0, 4)]))

m = np.array([[ 4, 6, -1,  8], \
              [11, 0, 16,  3], \
              [ 1, 3,  3,  9], \
              [-4, 4,  5, -3]])
# Домножение каждого элемента на элементы, расположенные в этой же строке и столбце
m2 = np.array([[reduce(lambda f, s: f * s, [*m[i, :], *m[:, j][: j], *m[:, j][j + 1 : ]]) for j in range(len(m[0]))] for i in range(len(m))])
print(m)
print(m2)
