def transpose(m):
    # transposes the matrix
    dummy = [[0 for i in range(len(m))] for j in range(len(m[0]))]
    for i in range(len(m[0])):  # nr_col
        for j in range(len(m)):  # nr_row
            dummy[i][j] = m[j][i]
    return dummy


def minor(matrix, i=0, j=0):
    # this minor function works!!!
    r = matrix.copy()
    del r[i]
    c = transpose(r)
    del c[j]
    ans = transpose(c)
    return ans

