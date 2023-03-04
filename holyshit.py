n = int(input())

matrix = list()
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

def print_matrix(matrix, row, col, width=1):
    for r in range(row):
        for c in range(col):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

flag = True
for i in range(n):
    for j in range(i+1,n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break
    if not flag:
        break

print('YES') if flag else print('NO')

