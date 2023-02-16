from random import choice
# XXX from global in func -> just boolean
# Code don't run now 15.02.2023
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
BAD_CHARS = 'il1Lo0O'

# Creat global var num_of_pass with num for passwords to generate

def pass_num():
    num_of_pass = input('Введите кол-во паролей для генерации: ')
    while not is_valid(num_of_pass):
        print('Нужно натуральное число!')
        num_of_pass = input('Введите кол-во паролей для генерации: ')    
    print('Кол-во паролей:', num_of_pass)
    return int(num_of_pass)

# Creat global var pass_length with length of password
def pass_length():
    pass_length = input('Введите длинну для пароля:  ')
    while not is_valid(pass_length):
        print('Нужно натуральное число!')
        pass_length = input('Введите длинну для пароля: ')    
    print('Длинна пароля:', pass_length)
    return int(pass_length)

# Включаем цифры в пароль?


def is_digit_in():
    if validate_answer('Включаем цифры в пароль?'):
        print('Цифры включены.')
        return True
    else:
        print('Пароль без цифр!')
        return False

# Включаем заглавные буквы в пароль?
def is_upper_in():
    if validate_answer('Включаем заглавные буквы в пароль?'):
        print('Заглавные буквы включены.')
        return True
    else:
        print('Пароль без заглавных букв!')

# Включаем строчные буквы в пароль?
def is_lower_in():
    if validate_answer('Включаем строчные буквы в пароль?'):
        print('Строчные буквы включены.')
        return True
    else:
        print('Пароль без строчных букв!')
        return False

# Включаем особые знаки (!#$%&*+-=?@^_ ) в пароль?
def is_punct_in():
    if validate_answer('Включаем особые знаки (!#$%&*+-=?@^_ ) в пароль?'):
        print('Особые знаки включены.')
        return True
    else:
        print('Пароль без особых знаков!')
        return False

# Исключать ли неоднозначные символы? (il1Lo0O)
def is_badchars_out():
    if validate_answer('Исключить неоднозначные символы (il1Lo0O) из пароля?'):
        print('Пароль без неоднозначных символов (il1Lo0O).')
        return True
    else:
        print('Неоднозначные символы присутствуют.')
        return False

# Transform answer yes or no to boolean or to -1 for any others
def is_valid_answer(txt):
    if txt == "y" or txt == "д":
        return True
    elif txt == "n" or txt == "н":
        return False
    else:
        return -1

# is_valid_answer with print
# return: always True or False
def validate_answer(question):
    yes_or_no = ' (y / д - для ДА, n / н - for no): '
    txt = input(question + yes_or_no)
    while is_valid_answer(txt) == -1:
        print('Введите y или д для ДА; n или н для НЕТ.')
        txt = input(question + yes_or_no)
    return is_valid_answer(txt)

# for n in [1:100]
def is_valid(text):
    return text.isdigit() and 0 < int(text) < 101


def is_not_all_no(dig, upp, low, punct):
    if not dig and not upp and not low and not punct:
        print('Пароль не может быть без знаков!')
        return False
    else:
        return True

def build_a_string(dig, upp, low, punct, bad_chars):
    chars = ''
    if dig:
        chars += DIGITS
        #print(pick_from_list)
    if upp:
        chars += UPPERCASE_LETTERS
        #print(pick_from_list)
    if low:
        chars += LOWERCASE_LETTERS
        #print(pick_from_list)
    if punct:
        chars += PUNCTUATION
        #print(pick_from_list)
    if bad_chars:
        return ''.join([x for x in chars if x not in BAD_CHARS])
    else:
        return chars

def loop_logic(txt, num_of_pass, pass_length):
    chars = ''
    for _ in range(num_of_pass):
        for _ in range(pass_length):
            chars += choice(txt)
        print(chars)
        chars = ''

# Main function
def main():
    
    from_start = True
    while from_start:
        num_of_pass = pass_num()
        len_of_pass = pass_length()
        digit_in = is_digit_in()
        upper_in = is_upper_in()
        lower_in = is_lower_in()
        punct_in = is_punct_in()
        bad_chars = is_badchars_out()
        ####### START LOGIK ########
        
        # if no characters are selected
        from_start = not is_not_all_no(digit_in, upper_in, lower_in, punct_in)
        if from_start:
            temp_from_start = validate_answer('Попробовать сначала?')
            if temp_from_start:
                # XXX ???
                #pass
                print('IM HERE')
                continue
            else:
                exit()

        # build a list from which we select characters
        list_from_pick = build_a_string(digit_in, upper_in, lower_in, punct_in, bad_chars)
        loop_logic(list_from_pick, num_of_pass, len_of_pass)


# Run code    
main()