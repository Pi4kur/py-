from random import *

random_num = randint(1,100)
counter = 1

def is_valid(text):
    return text.isdigit() and 0 < int(text) < 101

def compare_nums(user_num, random_num):
    if user_num < random_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        return True
    elif user_num > random_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        return True
    else:
        print('Вы угадали, поздравляем!')
        print('Число попыток:', counter)
        return False


# Start game
print('Добро пожаловать в числовую угадайку')

flag = True # not guess yet
while flag:
    text = input('Введите число от 1 до 100: ')
    n = 0
    if not is_valid(text):
        print('А может быть все-таки введем целое число от 1 до 100?')
        counter += 1
        continue
    else:
        n = int(text)
    flag = compare_nums(n,random_num)
    counter += 1
    if not flag:
        one_more_game = input('You wanna play another game? :) y for Yes - any for No: ')
        if one_more_game == 'y':
            flag = True
            counter = 1
            random_num = randint(1,100)
    
    

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')    

