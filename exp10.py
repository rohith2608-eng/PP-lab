# Define matrices
A = [[1, 2],
     [3, 4]]

B = [[4, 5],
     [6, 7]]

# Matrix Addition
addition = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    addition.append(row)

# Matrix Subtraction
subtraction = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] - B[i][j])
    subtraction.append(row)

# Transpose of Matrix A
transpose_A = []
for i in range(len(A[0])):
    row = []
    for j in range(len(A)):
        row.append(A[j][i])
    transpose_A.append(row)

# Display Results
print("Matrix A:")
for r in A:
    print(r)

print("\nMatrix B:")
for r in B:
    print(r)

print("\nAddition (A + B):")
for r in addition:
    print(r)

print("\nSubtraction (A - B):")
for r in subtraction:
    print(r)

print("\nTranspose of Matrix A:")
for r in transpose_A:
    print(r)
