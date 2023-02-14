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

