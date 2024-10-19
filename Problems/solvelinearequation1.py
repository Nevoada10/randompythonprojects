g_aug_mtrx = ([
    [1, 2, 3],
    [4, 5, 6]
])

"""
In each column, select a non-zero element as a pivot. If the pivot element is not at the top of the column, 
interchange rows to move the pivot element upwards.
"""


def find_pivot(aug_mtrx):
    matrix = aug_mtrx  # Changing variable name for shor
    n_rows, n_cols = matrix.shape  # Matrix shape = tuple of rows and columns of the matrix.
    pivots = []




find_pivot(g_aug_mtrx)
