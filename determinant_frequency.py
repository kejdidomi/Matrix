from MatrixShell import *

master = []
for k in range(3, 5):
    data = []
    cnt = []
    for i in range(100000):
        a = MatrixShell.random_i(k, k, -9, 9)
        data.append(a.det())

    for i in range(100):
        cnt.append(data.count(data[i]))

    print('Matrix size = ', k)
    print("determinant value most repeated: ", data[cnt.index(max(cnt))])
    print('number of times it was repeated: ', max(cnt))

    if data[cnt.index(max(cnt))] not in master:
        master.append(data[cnt.index(max(cnt))])

print(master)
