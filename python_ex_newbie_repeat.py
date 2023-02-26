# put your python code here
#a, b, c = float(input()), float(input()), float(input())
a, b, c = -5.64671390542564, 7.90460919676605, -2.10960556210672
diskrim = b**2 - 4 * a * c
if diskrim < 0:
    print("Нет корней")
elif diskrim == 0:
    print("D = 0")
    print(-b/2/a)
else:
    print("D > 0")
    x1 = (-b-(diskrim)**0.5)/2 / a
    x2 = (-b+(diskrim)**0.5)/2 / a
    print(min(x1,x2))
    print(max(x1,x2))


# put your python code here
num1, num2 = int(input()), int(input())
counter = 0
for i in range(num1, num2+1):
    if i**3 % 10 == 4 or i**3 % 10 == 9:
        print(i)
        counter += 1
print(counter)   

mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)


# for n in range(11):
#    for k in range(26):
#       for m in range(201):
#          if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
#             print(n, k, m)

iteration = 0
for a in range(1,28):
   for b in range(a,85):
      for c in range(b, 115):
         for d in range(c, 140):
            for e in range(d, 151):
               iteration += 1
               if e**5 > a**5 + b**5 + c ** 5 + d**5:
                  break
               elif b**5 + c**5 + d**5 - e**5 == -a**5:
                  print(a,b,c,d,e)
                  print("END! Iteration:", iteration)
                  quit()
               else:
                  print("false", a, b, c, d, e, "inter -->", iteration)


# 28
# 85
# 115
# 140
# 151
# put your python code here
#a,b=int(input()),int(input())
a,b=1,1000
max_num = a
max_count = 0
max_sum = 0

for i in range(a, b+1):
   print(i, " :i ", end=" ")
   temp_count = 0
   temp_sum = 0
   for j in range(1, i+1):
      print(j, " :j")
      print(i, "%", j, "=", i % j) 
      if i % j == 0:
         temp_count += 1
         temp_sum += j
         print("temp_count:",temp_count)
         print("temp_sum",temp_sum)
   if temp_sum >= max_sum:
      max_num = i
      print("gefunden max_num", i)
      print("from", max_count," to", temp_count)
      print("from", max_sum," to", temp_sum)
      max_count, max_sum = temp_count, temp_sum
print(max_num, max_sum)

# put your python code here7.9
n = 734573659783465783465978346593487
#n = int(input())

while n > 9:
    print("n: ", n)
    temp_n = n
    sum = 0
    while temp_n > 0:
        last_digit = temp_n % 10
        sum += last_digit
        temp_n = temp_n // 10
        
    n = sum

print(n)

a, b = int(input()), int(input())
for i in range(a, b + 1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag and i != 1:
        print(i)

a,b,c,d = 1,1,1,1
for i in range(a,35):
    for j in range(b,35):
        for k in range(c, 35):
            for l in range(d, 35):
                sum1, sum2 = i ** 3 + j ** 3, k ** 3 + l ** 3
                if sum1 == sum2 and i != j and i != k and i != l and j != k and j != l and k != l:
                    print("***** SUMMMMMM ********")
                    print(sum1)


s1 = 'foo bar foo baz foo qux'
print(s1.rfind(" z")) #-1
print(s1.rfind("z ")) #14


# exam 12

# put your python code here
#text = input()
#my_list = text.split('-')
#my_list = '7-301-447-5820'.split('-')
my_list = '301-4477-5820'.split('-')
print(my_list)
print(len(my_list))
flag = True
if len(my_list) != 3 and len(my_list) != 4: # after split have to be 3 or 4
    print('flag=false, not 3 or 4 elem')
    flag = False

if len(my_list) == 3 and flag: # if 3/ w/o first 7
    if len(my_list[0]) == 3 and len(my_list[1]) == 3 and len(my_list[2]) == 4:
        for st in my_list:
            if flag:
                for c in st:
                    if c not in "0123456789":
                        flag = False
                        break

    else:
       flag = False 

elif len(my_list) == 4 and flag: #4 elem -> with 7 at start
    print('4 elem after splitt')
    if my_list[0] == '7' and len(my_list[1]) == 3 and len(my_list[2]) == 3 and len(my_list[3]) == 4:
        print("7-xxx-xxx-xxxx")
        for st in my_list:
            if flag:
                for c in st:
                    if c not in "0123456789":
                        flag = False
                        break
    else:
        flag = False

if flag:
    print('YES')
else:
    print('NO')



##
my_list = list()

def merge(list1, list2):
    print(list1)
    print(list2)
    print(my_list)
    print("***********************")
    if not list1: #list1 is empty
        print("list 1 is empty")
        my_list.extend(list2)
        return my_list
    if not list2: #list2 is empty
        print("list 2 is empty")
        my_list.extend(list1)
        return my_list
    
    if list1[0] <= list2[0]:
        my_list.append(list1.pop(0))
        return merge(list1, list2)
    else:
        my_list.append(list2.pop(0))
        return merge(list1, list2)


numbers1 = [1, 7, 10, 16] #[int(c) for c in input().split()]
numbers2 = [5, 6, 13, 20] #[int(c) for c in input().split()]

# вызываем функцию 
print(merge(numbers1, numbers2))


# объявление функции
def is_palindrome(text):
    #delete all unwanted chars
    print(text)
    
    text1="".join(c for c in text if c.isalpha())
    print(text1)
    
    text1 = text1.casefold()
    print(text1)
    
    text_list_1 = list(text1)
    print(text_list_1)
    
    if text_list_1 == text_list_1[::-1]:
        return True
    else:
        return False

# считываем данные

txt = 'Карман, жена, но Какашкин - вор! О, Ковалева... Вела во коровник. Ша! Как она нежна! рак...' #input()

# вызываем функцию
print(is_palindrome(txt))


def is_correct_bracket(text):
    counter = 0
    for c in text:
        if c == ')' and counter == 0:
            return False
        if c == ')' and counter > 0:
            counter -= 1
        if c == '(':
            counter += 1
    return not counter




def convert_to_python_case(text):
    index_of_first_upper = 0
    result_string = ''
    for i in range(len(text)):
        if text[i].isupper():
            if i == index_of_first_upper:
                continue
            elif i > index_of_first_upper:
                if index_of_first_upper == 0:
                    result_string = text[:i]
                else:
                    result_string = result_string + '_' + text[index_of_first_upper:i]
                
                index_of_first_upper = i
    
    #last word
    result_string = result_string + '_' + text[index_of_first_upper:]
    result_string = result_string.casefold()
    return result_string

txt = 'MyMethodThatDoSomething'

print(convert_to_python_case(txt))

# Exam 14
def draw_triangle():
    for i in range(8):
        n_stars = i * 2 + 1
        n_whitespace = (15 - n_stars) // 2
        print(' ' * n_whitespace + '*' * n_stars + ' ' * n_whitespace)
        

#draw_triangle()

list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
list_11 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
list_21 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

def is_magic(date):
    list_num = date.split('.')
    print(*list_num)
    print(list_num[2][2:5])
    return int(list_num[0]) * int(list_num[1]) == int(list_num[2][2:5])

#print(is_magic('10.06.1960'))
#print(is_magic('11.06.1960'))
text = 'Jackdaws love my big sphinx of quartz'
string = ''.join(text.split())
print(string)
print(set(text))
print(set(string))
print(len(set(string)))

##########################
# BOH - Bin Oct Hex

hex = '1AF2'
dec = 513

#dec = int(hex, 16)
print(bin(dec))

########## Repeat ###########
# mass, height = float(input('Mass: ')), float(input('Height: '))
mass, height = 80, 1.76
IMT = mass / height ** 2
if IMT < 18.5:
    print('Недостаточная масса')
elif IMT > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')

#######

ANIMALS = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
year = int(input())
print(ANIMALS[abs(year - 2000) % 12])

############

fake_num = input()
if len(fake_num) == 5:
    print(fake_num[::-1].lstrip('0'))
elif len(fake_num) == 6:
    print((fake_num[0] + fake_num[-1:-6:-1]).lstrip('0'))

###################

# fake_num = input()

text = '100000000'
text_list = list(text)
print(text_list)

num_of_com = len(text_list)


def SAC(txt):
    lst = list()
    while len(txt) > 3:
        lst.append(txt[-3:])
        txt = txt[:-3]
    lst.append(txt)
    lst.reverse()
    return ','.join(lst)


#print(SAC(text))

# num have to be digit 
num = int(text)
print(f'{num:,}')

a = input()[: : -1]
print(",".join([a[ i: i + 3] for i in range(0, len(a), 3)])[ : : -1])


#########
num_of_dots = int(input())
list_of_dots = list()
for _ in range(num_of_dots):
    list_of_dots.append(input())



# Text like '3 4' / '-5 -9'
# return x, y: 3, 4 / -5, -9
def str_to_x_y(dots):
    lst = dots.split()
    return int(lst[0]), int(lst[1])

def which_quad(x, y):
    if x == 0 or y == 0:
        pass    
    elif x > 0 and y > 0:
        quad_1 += 1
    elif x < 0 and y > 0:
        quad_2 += 1
    elif x < 0 and y < 0:
        quad_3 += 1
    elif x > 0 and y < 0:
        quad_4 += 1

def main():
    quad_1 = 0
    quad_2 = 0
    quad_3 = 0
    quad_4 = 0
    for dots in list_of_dots:
        x, y = str_to_x_y(dots)
        if x == 0 or y == 0:
            pass    
        elif x > 0 and y > 0:
            quad_1 += 1
        elif x < 0 and y > 0:
            quad_2 += 1
        elif x < 0 and y < 0:
            quad_3 += 1
        elif x > 0 and y < 0:
            quad_4 += 1
    print('Первая четверть:', quad_1)
    print('Вторая четверть:', quad_2)
    print('Третья четверть:', quad_3)
    print('Четвертая четверть:', quad_4)

main()

####################
#num_str = input()
num_str = '6 5 8 79 8 57 69'
#list_num = num_str.split()
list_num = [int(x) for x in num_str.split()]
print(*list_num)
temp_num = list_num[0]
count = 0
for i in range(1,len(list_num)):
    if temp_num < list_num[i]:
        count += 1
        print('+', temp_num,list_num[i])
        temp_num = list_num[i]
    else:
        print('-', temp_num,list_num[i])
        temp_num = list_num[i]

print(count)
######################
#num_str = input()
num_str = '6 5 8 79 8 57 69'
#list_num = num_str.split()
#list_num = [int(x) for x in num_str.split()]
list_num = list(map(int, input().split()))

for i in range(len(list_num) // 2):
    list_num[i*2], list_num[i*2+1] = list_num[i*2+1], list_num[i*2]

print(*list_num)

#######################
# put your python code here
num_list = input().split() 
print(num_list[-1], *num_list[:-1])

#############
num = int(input())
num_list = list()
for i in range(num):
    num_list.append(int(input()))
num_to_proof = int(input())
flag = False
for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_to_proof == num_list[i] * num_list[j]:
            flag = True
            break
    if flag:
        break
print("ДА") if flag else print('НЕТ')

################
text = '0000a0000n00t00000o000000n'

def anton_in(txt):
    stage_a = False
    stage_n = False
    stage_t = False
    stage_o = False
    stage_2n = False
    for c in txt:
        if c == 'a':
            stage_a = True
            print('a gefunden')
        elif c == 'n' and stage_a and not stage_o:
            stage_n = True
            print('n nach a gefunden')
        elif c == 't' and stage_a and stage_n:
            stage_t = True
            print('t nach n gefunden')
        elif c == 'o' and stage_a and stage_n and stage_t:
            stage_o = True
            print('o gefunden')
        elif c == 'n' and stage_a and stage_n and stage_t and stage_o:
            stage_2n = True
            print('2. n gefunden')
    if stage_a and stage_n and stage_t and stage_o and stage_2n:
        return True
    else:
        return False

print(anton_in(text))

for i in range(num):
    if anton_in(input()):
        print(i, end=' ')


###########################
string = input() + ' запретил букву'
alpha = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for c in alpha:
    if len(string.strip()) != 0:
        if c in string:
            print(string.strip(), c)
            string = string.replace(c,'')
            string = string.replace('  ',' ')
    else:
        break
            