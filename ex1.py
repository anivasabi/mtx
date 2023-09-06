import random

def matrix1():
    a = int(input("First index matrix 1: "))
    b = int(input("Second index matrix 1: "))
    array = []
    for i in range(a):
        array.append([])
        for j in range(b):
            array[i].append(random.randint(1, 10))
    return array

def matrix2():
    a = int(input("First index matrix 2: "))
    b = int(input("Second index matrix 2: "))
    array = []
    for i in range(a):
        array.append([])
        for j in range(b):
            array[i].append(random.randint(1, 10))
    return array

def res(matrix1, matrix2):
    a = len(matrix1)
    b = len(matrix1[0]) 
    result = []
    for i in range(a):
        result.append([])
        for j in range(b):
            p = 0
            for k in range(len(matrix2)):
                p += matrix1[i][k] * matrix2[k][j]
            result[i].append(p)
    return result

mat1 = matrix1()
mat2 = matrix2()
result_matrix = res(mat1, mat2)

print("Matrix 1:")
for row in mat1:
    print(row)

print("Matrix 2:")
for row in mat2:
    print(row)

print("Result:")
for row in result_matrix:
    print(row)
