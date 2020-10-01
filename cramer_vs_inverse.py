# from MatrixShell import *
# import time
#
# a = MatrixShell.random_i(10, 10, -100, 100)
#
# b = MatrixShell(10, 1, 1)
# b.matrix = [[2], [0], [13], [-9], [-12], [-5], [0], [0], [-4], [-2]]
#
# s1 = time.time()
# ans = a.cramers([2, 0, 13, -9, -12, -5, 0, 0, -4, -2])
# f1 = time.time()
#
# s2 = time.time()
# c = a.inverse()*b
# f2 = time.time()
#
#
# print(ans)
# print('cramer time: ', f1-s1)
# print(c.matrix)
# print('inverse time: ', f2-s2)

# cramer is faster in this case 291 sek with 333 sek

from MatrixShell import *
import time

a = MatrixShell.random_i(9, 9, -100, 100)

b = MatrixShell(9, 1, 1)
b.matrix = [[2], [0], [13], [-9], [-12], [-5], [0], [0], [-4]]

s1 = time.time()
ans = a.cramers([2, 0, 13, -9, -12, -5, 0, 0, -4])
f1 = time.time()

s2 = time.time()
c = a.inverse()*b
f2 = time.time()


print(ans)
print('cramer time: ', f1-s1)
print(c.matrix)
print('inverse time: ', f2-s2)

# inverse faster this time with 31.1 sek vs 32.3
# inverse faster again with 30.5 sek vs 35.6 sek
