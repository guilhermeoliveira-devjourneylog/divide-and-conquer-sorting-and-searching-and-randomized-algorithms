def strassen_matrix_multiply(A, B):
    """
    Multiplies two 2x2 matrices using the Strassen algorithm.

    Parameters:
    - A (list): 2x2 matrix A.
    - B (list): 2x2 matrix B.

    Returns:
    - list: Result of the multiplication of A by B.
    """

    # Check if matrices are 2x2
    if len(A) != 2 or len(A[0]) != 2 or len(B) != 2 or len(B[0]) != 2:
        raise ValueError("Matrices must be 2x2")

    # Divide matrices into submatrices
    a11, a12, a21, a22 = A[0][0], A[0][1], A[1][0], A[1][1]
    b11, b12, b21, b22 = B[0][0], B[0][1], B[1][0], B[1][1]

    # Calculate intermediate products
    P1 = a11 * (b12 - b22)
    P2 = (a11 + a12) * b22
    P3 = (a21 + a22) * b11
    P4 = a22 * (b21 - b11)
    P5 = (a11 + a22) * (b11 + b22)
    P6 = (a12 - a22) * (b21 + b22)
    P7 = (a11 - a21) * (b11 + b12)

    # Calculate result submatrices
    result_upper_left = P5 + P4 - P2 + P6
    result_upper_right = P1 + P2
    result_lower_left = P3 + P4
    result_lower_right = P1 + P5 - P3 - P7

    return [
        [result_upper_left, result_upper_right],
        [result_lower_left, result_lower_right]
    ]

# Example matrices
matrix_X = [[2, 1], [1, 3]]
matrix_Y = [[4, 5], [6, 7]]

# Multiplication using Strassen
result_matrix = strassen_matrix_multiply(matrix_X, matrix_Y)

# Displaying the result
for row in result_matrix:
    print(row)
