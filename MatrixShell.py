class MatrixShell:
    def __init__(self, nr_row=0, nr_col=0, multiplication_instance=0):
        # initialization nothing new here
        self.nr_row = nr_row
        self.nr_col = nr_col
        if multiplication_instance == 1:
            pass
        else:
            if self.nr_row * self.nr_col != 0:
                self.matrix = self.populate()
            else:
                # this shit is cool
                code = compile('self.matrix = ' + input("enter matrix as you would with "
                                                        "python lists; i.e. [[1,2],[1, 2]:"), 'file', 'exec')
                exec(code)
                self.nr_row = len(self.matrix)
                self.nr_col = len(self.matrix[0])

    def __add__(self, other):
        if self.nr_row == other.nr_row and self.nr_col == other.nr_col:
            dummy = MatrixShell(len(self.matrix), len(self.matrix[0]), 1)
            dummy.matrix = [[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    dummy.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return dummy
        elif not isinstance(other, MatrixShell):
            print('Cannot add a MatrixShell with another type that is not MatrixShell!')
        else:
            print('Cannot add matrices with different dimensions!')

    def __radd__(self, other):
        if self.nr_row == other.nr_row and self.nr_col == other.nr_col:
            dummy = MatrixShell(len(self.matrix), len(self.matrix[0]), 1)
            dummy.matrix = [[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    dummy.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return dummy
        elif not isinstance(other, MatrixShell):
            print('Cannot add a MatrixShell with another type that is not MatrixShell!')
        else:
            print('Cannot add matrices with different dimensions!')

    def __sub__(self, other):
        if self.nr_row == other.nr_row and self.nr_col == other.nr_col:
            dummy = MatrixShell(len(self.matrix), len(self.matrix[0]), 1)
            dummy.matrix = [[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    dummy.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return dummy
        elif not isinstance(other, MatrixShell):
            print('Cannot add a MatrixShell with another type that is not MatrixShell!')
        else:
            print('Cannot subtract matrices with different dimensions!')

    def __rsub__(self, other):
        if self.nr_row == other.nr_row and self.nr_col == other.nr_col:
            dummy = MatrixShell(len(self.matrix), len(self.matrix[0]), 1)
            dummy.matrix = [[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    dummy.matrix[i][j] = other.matrix[i][j] - self.matrix[i][j]
            return dummy
        elif not isinstance(other, MatrixShell):
            print('Cannot add a MatrixShell with another type that is not MatrixShell!')
        else:
            print('Cannot subtract matrices with different dimensions!')

    def __mul__(self, other):
        # scalar or matrix multiplication,
        # usage: c = a * b where a and b are compatible matrices
        if isinstance(other, float) or isinstance(other, int):
            for i in range(self.nr_row):
                for j in range(self.nr_col):
                    self.matrix[i][j] *= other
            return self
        elif isinstance(self, MatrixShell) and isinstance(other, MatrixShell):
            if other.nr_row != self.nr_col:
                print('Incompatible')
                return

            else:
                new = MatrixShell(self.nr_row, other.nr_col, 1)

                def mul(c, d):
                    # creates a list with ordered entries of a matrix
                    # obtained from 2 other multiplied matrices
                    # starting from left to right
                    # a11,a12,a13...
                    # a21,a22,a23...
                    # ...
                    final = []

                    def m(x, y):
                        # creates a list which if you sum its elements
                        # you get elements of a matrix obtained from
                        # multiplication of 2 other matrices
                        dummy = []
                        for cnt in range(len(x)):
                            dummy.append(x[cnt] * y[cnt])
                        return dummy

                    for k in range(self.nr_row):
                        for g in range(other.nr_col):
                            final.append(sum(m(c[k], d[g])))
                    return final

                new.matrix = new.populate(2, mul(self.matrix, other.transpose().matrix))
                return new
        else:
            print("multiplying different variables")

    def __rmul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            for i in range(self.nr_row):
                for j in range(self.nr_col):
                    self.matrix[i][j] *= other
            return self
        else:
            print("multiplying different variables")

    def populate(self, d=1, lst1=None):
        # called in __init__() where it prompts the user for input
        # or called from __mul__() with d != 1 so it can use lists to create a new matrix (not input)
        if d == 1:
            lst = list(input("Enter the elements separated by a single comma: ").split(','))
        else:
            lst = lst1
        self.matrix = [[0 for i in range(self.nr_col)] for j in range(self.nr_row)]
        for i in range(self.nr_row):
            for j in range(self.nr_col):
                self.matrix[i][j] = float(lst.pop(0))
        return self.matrix

    def transpose(self):
        # transposes the matrix
        dummy = MatrixShell(len(self.matrix), len(self.matrix), 1)
        dummy.matrix = [[0 for i in range(self.nr_row)] for j in range(self.nr_col)]
        for i in range(len(self.matrix[0])):  # nr_col
            for j in range(len(self.matrix)):  # nr_row
                dummy.matrix[i][j] = self.matrix[j][i]
        return dummy

    @staticmethod
    def minor(matrix, i=0, j=0):
        # this minor function works!!!
        def transpose(m):
            # transposes the matrix, separated from MatrixShell
            dummy = [[0 for i in range(len(m))] for j in range(len(m[0]))]
            for i in range(len(m[0])):  # nr_col
                for j in range(len(m)):  # nr_row
                    dummy[i][j] = m[j][i]
            return dummy

        r = matrix.copy()
        del r[i]
        c = transpose(r)
        del c[j]
        ans = transpose(c)
        return ans

    def det(self):
        import determinant
        return determinant.determinant(self.matrix)

    def adjugate(self):
        from determinant import determinant
        from minor import minor, transpose
        matrix = self.matrix
        lst = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                lst.append((-1) ** (i + j) * determinant(minor(matrix, i, j)))

        dummy = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
        for k in range(len(matrix)):
            for g in range(len(matrix)):
                dummy[k][g] = lst.pop(0)

        r = MatrixShell(len(self.matrix), len(self.matrix), 1)
        r.matrix = transpose(dummy)
        return r

    def inverse(self):
        if self.det() != 0:
            return self.adjugate() * (1 / self.det())
        else:
            print('Determinant = 0, no inverse')
            return None

    @staticmethod
    def random_i(r, c, range_start=-10, range_end=10):
        import random
        s = range_start
        e = range_end
        dummy = MatrixShell(r, c, 1)
        dummy.matrix = [[random.randint(s, e) for i in range(c)] for j in range(r)]
        return dummy

    def cramers(self, vector):
        try:
            ans = []
            matrix_transposed = self.transpose().matrix
            d = self.transpose().det()
            for i in range(len(vector)):
                removed = matrix_transposed.pop(i)
                matrix_transposed.insert(i, vector)
                from determinant import determinant
                ans.append(determinant(matrix_transposed) / d)
                matrix_transposed.pop(i)
                matrix_transposed.insert(i, removed)

            return ans
        except ZeroDivisionError:
            return 'No solution (determinant = 0)'
