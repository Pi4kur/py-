from math import factorial
print(factorial(0))

def n_uber_m(n, m):
    return factorial(n)//(factorial(m) * factorial(n - m))

for i in range(5):
    print('n=', 4, 'm=', i, 'binkof=', n_uber_m(4,i))

def pascal(num):
    my_list = list()
    for i in range(num+1):
        my_list.append(n_uber_m(num,i))
    return my_list

print(*pascal(4))

###########################

text = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'

my_list = text.split()
print(my_list)
result_list = list()
last_char = '0'
temp_list = list()
for char in my_list:
    print(char)
    if char == last_char or len(temp_list) == 0:
        temp_list.append(char)
        print('YES:', temp_list)
    elif len(temp_list) > 0:
        result_list.append(temp_list)
        print('NO:', temp_list)
        print(result_list)
        temp_list = list()
        temp_list.append(char)
    
    last_char = char
if len(temp_list) > 0:
    result_list.append(temp_list)
    
print(result_list)
    
######################

my_list = input().split()
num = int(input())
result_list = list()
temp_list = list()

if num >= len(my_list):
    result_list.append(my_list)
else:
    for char in my_list:
        if len(temp_list) == num:
            result_list.append(temp_list)
            temp_list = list()
        temp_list.append(char)

if len(temp_list) > 0:
    result_list.append(temp_list)

print(result_list)

#########################

# my_list = input().split()
my_list = '1 2 3 0'.split()
length = len(my_list)

result_list = list()
result_list.append([])
temp_list = list()

for i in range(1, length + 1):
    for j in range(length - i + 1):
        result_list.append(my_list[j:j+i])

print(result_list)

###########################

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

############################

import sys

n = int(input())
matrix = list()
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
up, right, bot, left = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if i > j and i < n - j - 1:
            left += matrix[i][j]
        elif i < j and i > n - j - 1:
            right += matrix[i][j]
        elif i < j and i < n - j - 1:
            up += matrix[i][j]
        elif i > j and i > n - j - 1:
            bot += matrix[i][j]

print('Верхняя четверть:', up)
print('Правая четверть:', right)
print('Нижняя четверть:', bot)
print('Левая четверть:', left)

################################

import sys

row, col = int(input()), int(input())
matrix = list()
m_a_x = ~sys.maxsize
for i in range(row):
    temp = [int(num) for num in input().split()]
    if max(temp) > m_a_x:
        m_a_x = max(temp)
    matrix.append(temp)

def print_matrix(matrix, row, col, width=1):
    for r in range(row):
        for c in range(col):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

for i in range(row):
    for j in range(col):
        if matrix[i][j] == m_a_x:
            print(i, j)
            quit()

################################

row, col = int(input()), int(input())
matrix = list()
for i in range(row):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

i, j = input().split()
for r in matrix:
    r[i], r[j] = r[j], r[i]

def print_matrix(matrix, row, col, width=1):
    for r in range(row):
        for c in range(col):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

print_matrix(matrix, row, col)

#########################
#
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

#########################
#
n = int(input())

matrix = list()
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

result_matrix = list()

for i in range(n):
    temp = [matrix[n - j - 1][i] for j in range(n)]
    result_matrix.append(temp)

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


print_matrix(result_matrix, n)

#########################
#
# 8 bcs of shach
pos = input()
matrix = [['.' for i in range(8)] for j in range(8)]

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

def get_pos_from_input(pos):
    row = 8 - int(pos[1])
    col = pos[0]
    if col == 'a':
        col = 0
    elif col == 'b':
        col = 1
    elif col == 'c':
        col = 2
    elif col == 'd':
        col = 3
    elif col == 'e':
        col = 4
    elif col == 'f':
        col = 5
    elif col == 'g':
        col = 6
    elif col == 'h':
        col = 7
    return row, col


row, col = get_pos_from_input(pos)
matrix[row][col] = 'N'

# XXX kak ueban? 4.5.vorlast
# jump with knight
for _ in range(8):
    if col + 2 < 8:
        if row + 1 < 8:
            matrix[row + 1][col + 2] = '*'
        if row - 1 >= 0:
            matrix[row - 1][col + 2] = '*'
    if col - 2 >= 0:
        if row + 1 < 8:
            matrix[row + 1][col - 2] = '*'
        if row - 1 >= 0:
            matrix[row - 1][col - 2] = '*'
    if col + 1 < 8:
        if row + 2 < 8:
            matrix[row + 2][col + 1] = '*'
        if row - 2 >= 0:
            matrix[row - 2][col + 1] = '*'
    if col - 1 >= 0:
        if row + 2 < 8:
            matrix[row + 2][col - 1] = '*'
        if row - 2 >= 0:
            matrix[row - 2][col - 1] = '*'


print_matrix(matrix, 8)

#########################
#
n = int(input())
num_to_proof = None
matrix = list()

def initialize():
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    num_to_proof = sum(matrix[0])

def from_1_to_n2(n):
    flag = False
    for i in range(1, (n ** 2) + 1):
        flag = False
        print('For i:', i)
        for lst in matrix:
            if i in lst:
                flag = True
                print(i, 'in', lst)
                break
        if not flag:
            break
    print('From 1 to n2', flag)
    return flag


def proof_row(num_to_proof):
    for i in range(n):
        temp_sum = None
        for j in range(n):
            if temp_sum is None:
                temp_sum = matrix[i][j]
            else:
                temp_sum += matrix[i][j]
        if temp_sum!= num_to_proof:
            return False    
    return True

def proof_col(num_to_proof):
    for i in range(n):
        temp_sum = None
        for j in range(n):
            if temp_sum is None:
                temp_sum = matrix[j][i]
            else:
                temp_sum += matrix[j][i]
        if temp_sum!= num_to_proof:
            return False
    return True

def proof_diag(num_to_proof):
    temp_sum = None
    for i in range(n):
        if temp_sum is None:
            temp_sum = matrix[i][i]
        else:
            temp_sum += matrix[i][i]
    if temp_sum!= num_to_proof:
        return False
    return True

def proof_adiag(num_to_proof):
    temp_sum = None
    for i in range(n):
        if temp_sum is None:
            temp_sum = matrix[n-i-1][n-i-1]
        else:
            temp_sum += matrix[n-i-1][n-i-1]
    if temp_sum!= num_to_proof:
        return False
    return True

if proof_row(num_to_proof) and proof_col(num_to_proof) and proof_diag(num_to_proof) and proof_adiag(num_to_proof) and from_1_to_n2(n):
    print("YES")
else:
    print("NO")

initialize()
print(from_1_to_n2(n))

#########################
#
row, col = map(int, input().split())
matrix = [['.' for i in range(col)] for j in range(row)]

def print_matrix(matrix, row, col, width=1):
    for r in range(row):
        for c in range(col):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
        
#for 0, 2, 4, ... rows -> stars at 1, 3, 5, ...
for i in range(0,row,2):
    for j in range(1,col,2):
        matrix[i][j] = '*'
        
# for 1, 3, 5, ... rows -> stars at 0, 2, 4, ...
for i in range(1,row,2):
    for j in range(0,col,2):
        matrix[i][j] = '*'
        
        
print_matrix(matrix, row, col)

#########################
#
n = int(input())
matrix = [[0 for i in range(n)] for j in range(n)]

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

for i in range(n):
    matrix[i][n-i-1] = 1

for i in range(n):
    for j in range(n):
        if i > n - j - 1:
            matrix[i][j] = 2
            
print_matrix(matrix, n)

#########################
#
row, col = map(int, input().split())
matrix = [[2 for i in range(col)] for j in range(row)]

num = 1
for j in range(col):
    for i in range(row):
        matrix[i][j] = num
        num += 1
        
def print_matrix(matrix, row, col, width=1):
    for r in range(row):
        for c in range(col):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
        
print_matrix(matrix, row, col, 3)

#########################
#
n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i <= j and i <= n - j - 1 or i >= j and i >= n - j - 1:
            matrix[i][j] = 1
        
def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
        
print_matrix(matrix, n, 3)

#########################
#
row, col = map(int, input().split())
matrix = [[1 for _ in range(col)] for _ in range(row)]
# inizialize logic
num = 1

direction_x = 1 # -1, 0, 1
direction_y = 0 # -1, 0, 1

i, j = 0, 0

max_col = col
max_row = row
min_col = 0
min_row = 0

while num <= row * col:
    # print(num, 'in', i, j)
    matrix[i][j] = num
    num += 1
    if j + direction_x == max_col:
        # print('change from L R to U D')
        direction_x = 0
        direction_y = 1
        min_row += 1
    elif i + direction_y == max_row:
        # print('change from U D to R L')
        direction_x = -1
        direction_y = 0
        max_col -= 1
    elif j + direction_x < min_col:
        # print('change from R L to D U')
        direction_x = 0
        direction_y = -1
        max_row -= 1
    elif i + direction_y < min_row:
        # print('change from D U to L R')
        direction_x = 1
        direction_y = 0
        min_col += 1
    i += direction_y
    j += direction_x

def print_matrix(matrix, row, col, width=1):
    for r in range(row):
        for c in range(col):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

print_matrix(matrix, row, col, 3)

#########################
#
row_1, col_1 = map(int, input().split())
matrix_1 = []
for _ in range(row_1):
    temp = list(map(int, input().split()))
    matrix_1.append(temp)

input() # divider
row_2, col_2 = map(int, input().split())
matrix_2 = []
for _ in range(row_2):
    temp = list(map(int, input().split()))
    matrix_2.append(temp)
    
def sum_matrix(matrix_1, matrix_2, row, col):
    for i in range(row):
        for j in range(col):
            matrix_1[i][j] += matrix_2[i][j]
            
def mult_matrix(matrix_1, matrix_2, row_1, col_1, col_2): # row_2 == col_1
    result_mat = [[0 for _ in range(col_2)] for _ in range(row_1)]
    for i in range(row_1):
        for j in range(col_2):
            summ = sum(matrix_1[i][k] * matrix_2[k][j] for k in range(col_1))
            print(summ)
            result_mat[i][j] = summ
    return result_mat



def print_matrix(matrix, row, col, width=1):
    for r in range(row):
        for c in range(col):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

print('################################################################')
print_matrix(matrix_1, row_1, col_1)
print('################################################################')
print_matrix(matrix_2, row_2, col_2)
print('################################################################')

mat = mult_matrix(matrix_1, matrix_2, row_1, col_1, col_2)
print_matrix(mat, row_1, col_2)

#########################
#
def pow_matrix(matrix, pow_n):
    temp_mat = matrix.copy()
    for _ in range(1, pow_n):
        temp_mat = mult_matrix(temp_mat, matrix, n, n, n)
    return 

################################
# Matrix practical examination #
################################
