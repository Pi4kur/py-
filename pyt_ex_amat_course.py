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
import sys

n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)
m_a_x = ~sys.maxsize
    
for i in range(n):
    for j in range(n):
        if i >= n - j - 1:
            if matrix[i][j] > m_a_x:
                m_a_x = matrix[i][j]

print(m_a_x)

#########################

n = int(input())

matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

flag = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
            flag = False
            break
    if not flag:
        break

print('YES') if flag else print('NO')

#########################

n = int(input())

matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


flag = True
for num in range(1, n + 1):
    for i in range(n):
        if num not in matrix[i]:
            flag = False
            break
        # print([matrix[j][i] for j in range(n)], 'i', i)
        if num not in [matrix[j][i] for j in range(n)]:
            flag = False
            break

print('YES') if flag else print('NO')

#########################

row, col = get_pos_from_input(pos)
matrix[row][col] = 'Q'

# XXX kak ueban? 4.5.vorlast
# move queen
for i in range(8):
    if matrix[row][i] != 'Q': # for row where queen stand
        matrix[row][i] = '*'
    if matrix[i][col] != 'Q': # for col where queen stand
        matrix[i][col] = '*'
    if row - i >= 0 and col + i < 8 and matrix[row - i][col + i] != 'Q':
        matrix[row - i][col + i] = '*'
    if row - i >= 0 and col - i >= 0 and matrix[row - i][col - i] != 'Q':
        matrix[row - i][col - i] = '*'
    if row + i < 8 and col + i < 8 and matrix[row + i][col + i]!= 'Q':
        matrix[row + i][col + i] = '*'
    if row + i < 8 and col - i >= 0 and matrix[row + i][col - i]!= 'Q':
        matrix[row + i][col - i] = '*'

print_matrix(matrix, 8)

#########################

n = int(input())

matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i - j)

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


print_matrix(matrix, n)

#########################
#
n = int(input())

matrix = []
for _ in range(n):
    name, num = input().split()
    matrix.append((name, int(num)))
lst = tuple(matrix)
print(lst)

for tp in lst:
    print(*tp)
print()
for tp in lst:
    if tp[1] > 3:
        print(*tp)

#########################
# HOLY SHIT
n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

n_and_m = m + n - x - t
n_and_k = n + k - z - t
m_and_k = m + k - y - t
only_n = n - t - n_and_m - n_and_k
only_m = m - t - n_and_m - m_and_k
only_k = k - t - n_and_k - m_and_k
print(only_k + only_m + only_n)
print(n_and_m + n_and_k + m_and_k)
print(a - (t + n_and_m + n_and_k + m_and_k + only_k + only_m + only_n))


n = int(input())
myset = {int(x) for x in input()}
for _ in range(n - 1):
    temp = {int(x) for x in input()}
    # print(temp)
    myset &= temp
    # print(myset)

print(*sorted(myset))

#########################
set1 = {int(x) for x in input().split()}
set2 = {int(x) for x in input().split()}
set3 = {int(x) for x in input().split()}

set4 = (set1 | set2) - set3
set5 = (set1 | set3) - set2
set6 = (set2 | set3) - set1

print(*sorted(set4 | set5 | set6))

sentence = ''
{word.strip(':,.!?();').lower() for word in sentence.split() if len(word.strip(':,.!?();').lower()) < 4}
files = []


{file.lower() for file in files if file[-4:].lower() == '.png'}

#########################
# Exam sets #############
# 18.03
m = int(input())
result_set = None
for _ in range(m):
    num = int(input())
    myset = {input() for _ in range(num)}
    if result_set is None:
        result_set = myset
    else:
        result_set &= myset

print(*sorted(result_set), sep='\n')

#########################
# Dictionary ############
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
names = tuple()

for user in users:
    if user['email'] == '' or 'email' not in user:
        names += (user['name'],)

print(*sorted(names))

#########################
#
d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
n = int(input())
tupl = ()
while n > 0:
    digit = n % 10
    n //= 10
    tupl += d[digit],
print(*reversed(tupl))

########################
#
d = {
    1 : '.,?!:',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ',
    0: ' '
}
string = input().upper()
for c in string:
    for a, b in d.items():
        if c in b:
            index = b.index(c) + 1
            print(str(a) * index, end='')
            break

#########################
#
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

string = input('Enter a string: ').upper()

for c in string:
    if c in letters:
        index = letters.index(c)
        print(morse[index], end=' ')

#########################
#
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

for a, b in dict2.items():
    if a in dict1.keys():
        dict1[a] += dict1.setdefault(a,b)
    else:
        dict1.setdefault(a,b)
result = dict1

#########################
#
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
result = {}
for word in s.split():
    if word in result:
        result[word] += 1
    else:
        result[word] = 1
print(result)
ma_x = max(result.values())
res = {}
for word, count in result.items():
    if count == ma_x:
        res.setdefault(word, count)
print(res)
print(sorted(res.keys())[0])

#########################
#
words = [word.strip('.,!?:;-') for word in input().lower().split()]

result = {}

for word in words:
    if word not in result:
        result.setdefault(word, 1)
    else:
        result[word] += 1
        
mi_n = min(result.values())
res = {}
for word, count in result.items():
    if count == mi_n:
        res.setdefault(word, count)
        
print(sorted(res.keys())[0])        

#########################
#
lst = input().split()

my_dict = {}

for s in lst:
        count = my_dict.setdefault(s, 0)
        print(s, end=' ') if count == 0 else print(f'{s}_{str(count)}', end=' ')
        my_dict[s] = count + 1


#########################
#
n = int(input())

my_dict = {}
for _ in range(n):
    a, b = input().split(': ')
    a = a.lower()
    my_dict[a] = b

m = int(input())
search = ()
for _ in range(m):
    word = input().lower()
    search += (word,)

for word in search:
    if word in my_dict:
        print(my_dict[word])
    else:
        print('Не найдено')

################################################################
#
word1 = tuple(x for x in input().lower() if x.isalpha())
word2 = tuple(x for x in input().lower() if x.isalpha())

print('YES') if sorted(word1) == sorted(word2) else print('NO')

################################
#
n = int(input())

my_dict = {}
for _ in range(n):
    a, b = input().split()
    my_dict[a] = b

m = int(input())

search_tub = ()
for _ in range(m):
    search = input().title()
    search_tub += (search,)

for search in search_tub:
    if search in my_dict.values():
        sym = (k for k, v in my_dict.items() if search.lower() == v.lower())
        print(*sym)
    else:
        print('абонент не найден')
        
################################
#
text, n = input(), int(input())
my_dict = {}

for _ in range(n):
    char, freq = input().split(': ')
    my_dict[char] = freq

code_dict = {}

for c in text:
    code_dict[c] = code_dict.setdefault(c, 0) + 1

for c in text:
    rep_c = [k for k, v in my_dict.items() if int(v) == code_dict[c]]
    print(*rep_c, end='')

##################################
#
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

result = {int(num): word for num, word in [paar.split(':') for paar in s.split()]}

result = {num: sorted([x for x in range(1,num + 1) if num % x == 0]) for num in numbers}

result = {word: [ord(c) for c in word] for word in words}

print(*result)

##################################
# DICT COMPREHENSIONS
numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]


# result = {num: sorted([x for x in range(1,num + 1) if num % x == 0]) for num in numbers}

# result = {word: [ord(c) for c in word] for word in words}

students = {}
remove_keys = []
# result = {k: v for k, v in letters.items() if k not in remove_keys}

# result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}

tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]

# result = {f: tuple(last) for f, *last in tuples}

student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

# result = [{a: {b: c}} for a, b, c in zip(student_ids, student_names, student_grades)]


# my_dict = {k:[x for x in v if x <= 20] for k, v in my_dict.items()}

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
l = []
for dom, names in emails.items():
    l.extend(f'{name}@{dom}' for name in names)
print(*sorted(l), sep='\n')

##################################
#
d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

text = input()
result = 0
for c in text:
    for key in d:
        if c in d[key]:
            result += key

print(result)

##################################

def build_query_string(dct: dict):
    lst = [str(f'{k}={dct[k]}') for k in sorted(dct.keys())]
    return '&'.join(lst)

def merge(lst_dict):
    result = {}
    for dct in lst_dict:
        for k, v in dct.items():
            result[k] = result.setdefault(k, set()) | {v,}
    return result

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)

##################################
n = int(input())

commands = {'write': 'W', 'read': 'R', 'execute': 'X'}

my_dict = {}

for _ in range(n):
    fl_name, *comms = input().split()
    my_dict[fl_name] = comms

m = int(input())
answers = []
for _ in range(m):
    com, fl_name = input().split()
    if commands[com] in my_dict[fl_name]:
        answers.append('OK')
    else:
        answers.append('Access denied')



# print(my_dict)

################################################################

n = int(input())
my_dict = {}

for _ in range(n):
    name, item, amount = input().split()
    if name in my_dict:
        my_dict[name] |= {item: int(amount) + my_dict[name].get(item, 0)}
    else:
        my_dict[name] = {item: int(amount)}
# print(my_dict)

for key in sorted(my_dict.keys()):
    print(f"{key}:")
    for k in sorted(my_dict[key].keys()):
        print(k, my_dict[key].get(k))

################################################################
import random

length = int(input())

for _ in range(length):
    num1 = random.randint(65, 90)
    num2 = random.randint(97, 122)
    choice = random.choice((num1, num2))
    print(chr(choice), end='')

################################################################
import random
lst = []
while len(lst) < 7:
    num = random.randint(1,49)
    if num not in lst:
        lst.append(num)
print(*sorted(lst))
################################################################
import random
import string

def generate_ip():
    return '.'.join([str(random.randrange(256)) for _ in range(4)])

upper = string.ascii_uppercase

def generate_index():
    index = random.choice(upper)
    index += random.choice(upper)
    index += f'{random.randrange(100)}_'
    index += str(random.randrange(100))
    index += random.choice(upper)
    index += random.choice(upper)
    return index

import random
matrix = []
lst = []
while len(lst) < 25:
    num = random.randint(1, 75)
    if num not in lst:
        lst.append(num)

for i in range(5):
    temp = lst[i*5:i*5 + 5]
    matrix.append(temp)
    
matrix[2][2] = 0

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

print_matrix(matrix, 5, 3)

########################################################################
import string
import random

BAD_CHARS = 'lI1oO0'

LET_AND_DIG = string.ascii_letters + string.digits

n, m = int(input()), int(input())

def validate_password(password):
    lower_in = False
    upper_in = False
    digit_in = False
    for c in password:
        if c.isdigit():
            digit_in = True
        elif c.islower():
            lower_in = True
        elif c.isupper():
            upper_in = True
    return lower_in & upper_in & digit_in

def generate_password(length):
    pw = ''
    while len(pw) < length:
        char = random.choice(LET_AND_DIG)
        if char not in BAD_CHARS:
            pw += char
    return pw if validate_password(pw) else generate_password(length)

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

print(*generate_passwords(n, m), sep='\n')

################################

import random

n = 10**6
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if x**2 + y**2 <= 1:
        k += 1

print((k/n)*s0)

################################################################

from fractions import Fraction as F
from math import gcd as gcd

n = int(input())
lst = []
for chis in range(1, n // 2 + n % 2):
    znam = n - chis
    print(chis, znam, ':', gcd(chis, znam))
    if chis >= znam:
        break
    if gcd(chis, znam) == 1:
        lst.append(F(chis, znam))

print(max(lst))

################################################################

from fractions import Fraction as F
from math import gcd as gcd

n = int(input())
lst = []
for chis in range(1, n):
    lst.extend(
        F(chis, znam) for znam in range(n, chis, -1) if gcd(chis, znam) == 1
    )

print(*sorted(lst), sep='\n')

################################################################
# SHORTER SOLUTION
from fractions import Fraction as F
from math import gcd as gcd

n = int(input())
lst = []

lst.extend(
    F(chis, znam) for chis in range(1, n) for znam in range(n, chis, -1) if gcd(chis, znam) == 1
)

print(*sorted(lst), sep='\n')

################################################################
import turtle as t

def draw_line(size):
    t.backward(size // 2)
    t.forward(size)
    t.backward(size // 2)

def result(size):
    for _ in range(6):
        draw_line(size)
        t.left(30)

result(200)

def draw_star(size):
    t.forward(size // 2)
    t.right(144)
    t.forward(size)
    t.right(144)
    t.forward(size)
    t.right(144)
    t.forward(size)
    t.right(144)
    t.forward(size)
    t.right(144)
    t.forward(size // 2)


import turtle

turtle.Screen().setup(400, 400)               # устанавливаем размер граф. окна
turtle.Screen().addshape('rocketship.png')    # добавляем форму черепашки

turtle.Screen().bgpic('space.jpg')            # устанавливаем фоновое изображение
turtle.shape('rocketship.png')                # устанавливаем форму черепашки
turtle.pencolor('green')
turtle.pensize(5)

for _ in range(4):
    turtle.forward(150)
    turtle.left(90)

################################################################
from turtle import dot as d, forward as f, left as l
[[d(10), f(s), l(90)] for s in (150, 75) * 2]

################################################################
import turtle
from random import randrange

def move_turtles(turtles, dist, angle):
    for turtle in turtles:    # все черепашки из списка делают одни и те же действия
        turtle.forward(dist)
        turtle.right(angle)


turtles = []                   # список черепашек
head = 0
num_turtles = 10               # количество череашек
for i in range(num_turtles):
    turt = turtle.Turtle()     # создаем черепашку и устанавливаем ее свойства
    turt.setheading(head)
    turt.pensize(2)
    turt.color(randrange(256), randrange(256), randrange(256))
    turt.speed(5)
    turt.tracer(25, 0)
    turtles.append(turt)       # добавляем черепашку в список
    head = head + 360/num_turtles

for i in range(70):
    move_turtles(turtles, 10, i)

################################################################
# Changes since Python 2.6 The methods Turtle.tracer(), Turtle.window_width() and Turtle.window_height() have been eliminated. Methods with these names and functionality are now available only as methods of Screen.
################################################################
import turtle
from random import randrange


screen = turtle.Screen()
screen.colormode(255)
screen.tracer(0)

def move_turtles(turtles, dist, angle):
    for turtle in turtles:    # все черепашки из списка делают одни и те же действия
        turtle.forward(dist)
        turtle.right(angle)


turtles = []                   # список черепашек
head = 0
num_turtles = 10               # количество череашек
for i in range(num_turtles):
    turt = turtle.Turtle()     # создаем черепашку и устанавливаем ее свойства
    turt.setheading(head)
    turt.pensize(2)
    turt.color(randrange(256), randrange(256), randrange(256))
    turt.speed(5)
    turtles.append(turt)       # добавляем черепашку в список
    head = head + 360/num_turtles

for i in range(70):
    move_turtles(turtles, 10, i)

turtle.mainloop()

################################################################

from turtle import *
bgcolor('darkblue'), penup(), speed(0)  # Настройка основных значений
dot(200, 'gold3'), forward(200)  # Рисование луны
shape('circle'), shapesize(10), color('darkblue')  # Настройка вида черепашки
while True:  # Цикл прохода черепашки справа налево
    for _ in range(400):
        backward(1)
    forward(400)

################################################################

def matrix(row=1, col=None, value=0):
    if col is None:
        col = row
    return [[value for _ in range(col)] for _ in range(row)]

################################################################

from math import sin
n = int(input())
func = input()

func_dict = {
    'квадрат': lambda x: x ** 2,
    'куб': lambda x: x ** 3,
    'корень': lambda x: x ** 0.5,
    'модуль': abs,
    'синус': sin
    }

print(func_dict[func](n))

################################################################

# put your python code here
numbers = input().split()

lst = [list(map(int, list(x))) for x in numbers]
dict_of_digit = dict(zip(numbers, lst))

def comparer(dic):
    return sum(dic[1])

my_dict = dict(sorted(dict_of_digit.items(), key=comparer))

print(*my_dict.keys())

# second solution in 1 line
# !!!!!!!!!!!!!!!!!!!!!!!!!

print(*sorted(input().split(), key=lambda x: sum(map(int, x))))

################################################################

print(*sorted(sorted(input().split(), key=lambda n: int(n)), key=lambda x: sum(map(int, x))))

################################################################

def map(function, items):
    return [function(item) for item in items]

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

n_num = map(lambda x: round(x,2), numbers)

print(*n_num, sep='\n')

################################################################

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

def ex_filt(num):
    return 99 < num < 1000 and num % 5 == 2

def cube(num):
    return num ** 3

nums = map(cube, filter(ex_filt, numbers))

print(*nums, sep='\n')

################################################################

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc

def map(function, items):
    return [function(item) for item in items]

nums_map = sum(map(lambda x: x ** 2, numbers))


numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

def add_sqr(x, y):
    return x + y ** 2

nums_red = reduce(add_sqr, numbers, 0)

print(nums_red)
print(nums_map)

################################################################

# Напишите программу для вычисления и вывода суммы квадратов двузначных чисел, которые делятся на 7 без остатка.

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

def ex_filter(num):
    return len(str(abs(num))) == 2 and num % 7 == 0

nums = sum(map(lambda x: x ** 2, filter(ex_filter, numbers)))
print(nums)

################################################################

from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

test_lst = list(sorted((map(lambda lst: lst[0], 
                        filter(lambda lst: lst[1] > 10000000 and lst[2] == 'primary', data)))))

print(reduce(lambda x, y: f'{x}, {y}', test_lst[1:], f'Cities: {test_lst[0]}'))

################################################################

is_num = (
    lambda x: x.replace('-', '', 1).replace('.', '', 1).isdigit()
    if x.startwith('-')
    else x.replace('.', '', 1).isdigit()
)

################################################################

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
sort_data = sorted(data, key=lambda x: x[1][-1], reverse=True)
print(*(f'{x[1]}: {x[0]}' for x in sort_data), sep='\n')

################################################################

mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']

print(*sorted(mixed_list, key=lambda x: (type(x) == str, x)))
# 0 1 3 5 8 a aab ab ac c

################################################################

from functools import reduce
coeff = [int(x) for x in input().split()]
x = int(input())

def evaluate(coefficients, x):
    return reduce(lambda k, i: k + i, 
                  map(lambda l, m: l * x ** m, coefficients, list(range(len(coefficients) - 1, -1, -1))))

print(evaluate(coeff, x))

################################################################

countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

print(*(f'{a} is the capital of {b}, population equal {c} people.' for a, b, c in zip(capitals, countries, population)), sep='\n')

################################################################

lst = list(input().split('.'))

print(all(map(lambda x: x.isdigit() and int(x) in range(256), lst))) # int(x) in range(256)

################################################################

a, b = int(input()), int(input())

def valuate(num):
    return all(map(lambda x: int(x) and num % int(x) == 0, set(str(num))))

print(*filter(lambda num: valuate(num), range(a, b + 1)))

################################################################
pw = input()

print('YES') if len(pw)> 6 and any(map(lambda x: x.islower(), pw)) and any(map(lambda x: x.isdigit(), pw)) and any(map(lambda x: x.isupper(), pw)) else print('NO')

################################################################

num_classes = int(input())
all_classes = []
for _ in range(num_classes):
    num_stud = int(input())
    clas_s = tuple(input().split()[1] == '5' for _ in range(num_stud))
    all_classes.append(clas_s)

print('YES') if all(map(any, all_classes)) else print('NO')


# all(map(lambda x: any(map(lambda x: x[1] == '5', x))

################################################################
# FILES
name = input()
with open(name, encoding='utf-8') as file:
    lst = file.readlines()
print(lst[-2])

################################################################

with open('prices.txt', encoding='utf-8') as file:
    lst = list(map(lambda x: x.rstrip().split('\t'), file.readlines()))

print(sum(map(lambda x: int(x[1]) * int(x[2]), lst)))

################################################################

with open('data.txt', encoding='utf-8') as file:
    lst_str = [x.strip() for x in file.readlines()]
    print(*iter(lst_str[::-1]), sep='\n')
    file.seek(0)
    lst_str_2 = file.readlines()
    print(*lst_str_2[::-1], sep='')

################################################################

def sum_line(line):
    return sum(int(x) for x in line.split())

with open('numbers.txt', encoding='utf-8') as file:
    print(*map(sum_line, file.readlines()), sep='\n')

################################################################

with open('data.txt', encoding='utf-8') as file:
    text = file.read()
    letters = len([x for x in text if x.isalpha()])
    words = len(text.split())
    lines = text.count('\n') + 1
    
    print('Input file contains:')
    print(letters, 'letters')
    print(words, 'words')
    print(lines, 'lines')

################################################################

with open('population.txt', encoding='utf-8') as file:
    text_lst = file.readlines()
    my_lst = [x.split('\t') for x in text_lst]
    print(my_lst)
    print(*map(lambda x: x[0], filter(lambda x: x[0].startswith('G') and int(x[1].strip()) > 500_000, my_lst)), sep='\n')
    
################################################################

def read_csv():
    with open('data.csv', encoding='utf-8') as file:
        keys = file.readline().strip().split(',')
        values_lst = file.readlines()
        return [dict(zip(keys, values.strip().split(','))) for values in values_lst]
        # return [dict(zip(keys, values.strip().split(','))) for values in file.readlines()] -> values_lst not needed

print(read_csv())

################################################################

with open('class_scores.txt', 'r', encoding='utf-8') as inputfile:
    with open('new_scores.txt', 'w', encoding='utf-8') as output:
        for line in inputfile:
            a, b = line.split()
            b = min(int(b.strip()) + 5, 100)
            output.write(f'{a} {b}\n')

################################################################


################################################################


################################################################


################################################################


################################################################



################################################################

