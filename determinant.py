from typing import Union
matrix = list[list[Union[int, float]]]


cache = {}
def matrix_determinant(mat_a: matrix, round_int: int = 2) -> float:
    """Calculates the determinant of a matrix. Uses a recursive function until it finds a 2x2 matrix
    
    
    Args:
    --------
        `mat_a (matrix)`: any matrix
        `round_int`: how many decimal places to round to. Default: 2
    
    
    Returns:
    --------
        `float`: matrix determinant
    
    Examples:
    --------
    >>> matrix_determinant([[1, 2], [3, 4]])
    >>> output: -2
    --------
    >>> matrix_determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> output: 0
    --------
    >>> matrix_determinant([[1, 3, 1, 4], [3, 9, 5, 15], [0, 2, 1, 1], [0, 4, 2, 3]])
    >>> output: -4
    """
    #? checking if its a valid and square matrix
    if not isinstance(mat_a, list):
        raise TypeError("Not a valid matrix.")
    if len(mat_a) != len(mat_a[0]):
        raise ValueError("Not a square matrix.")
    
    #? if the matrix is a 1x1, return the value
    if len(mat_a) == 1 and len(mat_a[0]) == 1:
        return mat_a[0][0]
    
    if len(mat_a) == 2:
        return mat_a[0][0] * mat_a[1][1] - mat_a[0][1] * mat_a[1][0]
    
    if str(mat_a) in cache:
        return cache[str(mat_a)]
    else:
        cache[str(mat_a)] = None
    
    soma: float = 0
    for i in range(len(mat_a)):
        soma += (-1)**i * mat_a[0][i] * matrix_determinant(matrix_submatrix(mat_a, i))
    cache[str(mat_a)] = round(soma, round_int)
    return cache[str(mat_a)]


def matrix_submatrix(mat_a: matrix, column: int) -> matrix:
    """Used internally by matrix_determinant(). Given a matrix of size `n` x `n`, returns a matrix of size `n-1` x `n-1` where
    we remove the row and column of the value of `matriz[0][column]`
    
    Args:
    --------
    mat_a (matriz): any matrix of size `n` x `n`
    column (int): the column of the value to be removed
    
    Returns:
    --------
        matriz: a matrix of size `n-1` x `n-1`
    
    Examples:
    --------
    >>> matrix_submatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0)
    >>> output: [[5, 6], [8, 9]]
    --------
    >>> matrix_submatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
    >>> output: [[1, 3], [7, 9]]
    """
    matriz_retorno: matrix = []
    for linha in mat_a[1:]:
        matriz_retorno.append([])
        for val, col in enumerate(linha):
            if val != column:
                matriz_retorno[-1].append(col)
    return matriz_retorno
