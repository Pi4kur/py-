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