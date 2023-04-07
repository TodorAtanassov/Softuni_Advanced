def find_position(rows):
    for row in range(rows):
        if 'Y' in matrix[row]:
            col = matrix[row].index('Y')
            return row, col


matrix_rows, matrix_cols = [int(x) for x in input().split(',')]
matrix = [[col for col in input().split()] for row in range(matrix_rows)]

position = find_position(matrix_rows)
print(position)
