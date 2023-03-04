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

