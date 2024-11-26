def ex1(arr):
    n = len(arr)
    if(n < 2):
        return False
    for i in range(n):
        for j in range(n):
            if(arr[i]+1 == arr[j]):
                return True
    return False


#print(ex1([1,3,7,4]))
#print(ex1([1,5,3]))



def print_columns(matrix):
    columns = len(matrix[0])
    for col in range(columns):
        column = [row[col] for row in matrix]  
        print(column)


matrix1 = [
    [1,2,3],
    [4,5,6]
]
#print(len(matrix1[0])) #should print 3
#print_columns(matrix1)


def check_if_symmetric(matrix):
    n = len(matrix[0])
    #check if sqaure
    for row in matrix:
        if (len(row) != n):
            return False
        
    for i in range(n):
        for j in range(n):
            if(matrix[i][j] != matrix[j][i]):
                return False
    return True

matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix3 = [
    [1,2,3],
    [2,5,6],
    [3,6,9]
]

def check_if_magic_matrix(matrix):
    n = len(matrix[0])
    #check if sqaure
    for row in matrix:
        if (len(row) != n):
            return False
    magic_number = sum(matrix[0])

    # Check sums of rows
    for row in matrix:
        if sum(row) != magic_number:
            return False
        
    #check sums of columns
    for col in range(n):
        if (sum(matrix[row][col] for row in range(n)) != magic_number):
            return False
        
    return True

matrix4 = [
    [2,7,6],
    [9,5,1],
    [4,3,8]
]
matrix5 = [
    [1,3],
    [2,4]
]
print(check_if_magic_matrix(matrix4))
print(check_if_magic_matrix(matrix5))



