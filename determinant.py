from minor import minor


def det1x1(matrix):
    return matrix[0][0]


def det2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def det3x3(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    return a * e * i + b * f * g + c * d * h - c * e * g - a * f * h - b * d * i


def det4x4(matrix):
    ans = 0
    depth = 4
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det5x5(matrix):
    ans = 0
    depth = 5
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det6x6(matrix):
    ans = 0
    depth = 6
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det7x7(matrix):
    ans = 0
    depth = 7
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det8x8(matrix):
    ans = 0
    depth = 8
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det9x9(matrix):
    ans = 0
    depth = 9
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det10x10(matrix):
    ans = 0
    depth = 10
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det11x11(matrix):
    ans = 0
    depth = 11
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det12x12(matrix):
    ans = 0
    depth = 12
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det13x13(matrix):
    ans = 0
    depth = 13
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det14x14(matrix):
    ans = 0
    depth = 14
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det15x15(matrix):
    ans = 0
    depth = 15
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det16x16(matrix):
    ans = 0
    depth = 16
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det17x17(matrix):
    ans = 0
    depth = 17
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det18x18(matrix):
    ans = 0
    depth = 18
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


def det19x19(matrix):
    ans = 0
    depth = 19
    row = matrix[0]
    for i in range(len(matrix[0])):
        ans += (-1) ** i * row[i] * det[depth - 1](minor(matrix, 0, i))
    return ans


det = [0, det1x1, det2x2, det3x3, det4x4, det5x5,
       det6x6, det7x7, det8x8, det9x9, det10x10,
       det11x11, det12x12, det13x13, det14x14,
       det15x15, det16x16, det17x17, det18x18, det19x19]


def determinant(matrix):
    return det[len(matrix)](matrix)



