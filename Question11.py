exec(f"matrix = {input('matrix: ')}")
matrix : list

r = int(input("Rows: "))
c = int(input("Columns: "))

def reshape(matrix, r, c):
    if r*c != len(matrix)*len(matrix[0]):
        return matrix
    
    flattened_matrix = []
    for i in matrix:
        flattened_matrix += i
    
    matrix = []
    for i in range(r):
        matrix.append(flattened_matrix[i*c : (i+1)*c])

    return matrix

print(reshape(matrix, r, c))