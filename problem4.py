def diagonal_differences(matrix):
    n = len(matrix)
    primary = sum(matrix[i][i] for i in range(n))
    secondary = sum(matrix[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)

matrix1 = [
    [2, 3, 4],
    [4, 5, 6],
    [9, 8, 9]
]

matrix2 = [
    [2, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(diagonal_differences(matrix1))
print(diagonal_differences(matrix2))  
