import numpy

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
#
# ab = []
#
# for i in range(0, len(a)):
#     ab.append(a[i] * b[i])
#
#
# print(ab)

import numpy as np

# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# c = a * b
# print(c)
#
# f = np.zeros(10, dtype=int)
# d = np.ones(10,dtype=int)
#
# print(f)
# print(d)
#
# g = np.random.randint(0, 10, size=15)
#
# print(g)

h = np.random.randint(0, 20, size=(7, 8))

print("------------------------",h,"------------------------")

j = np.random.randint(0, 20, size=(7, 8))

print("------------------------------------",j,"-------------------------")

k = h*j

print(k)
