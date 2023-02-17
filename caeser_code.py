eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

symbols = list(' ,.-!?"0123456789')

# encrypt or decode
# decode_version = input('You wann encrypt (e) or decode (d)? ')
# lang = input('Russia (ru) or English (en)? ')
# key = int(input('Step for decode: '))
# txt = input('Your phrase \n')

def decode(key, phrase, lang):
    result_phrase = ''
    if lang == 'en':
        mod = 26
    elif lang == 'ru':
        mod = 32
    for c in phrase:
        work_string = ''
        if c in symbols:
            result_phrase += c
            continue
        if c.isupper() and mod == 26:
            work_string = eng_upper_alphabet
        elif c.isupper() and mod == 32:
            work_string = rus_upper_alphabet
        elif c.islower() and mod == 26:
            work_string = eng_lower_alphabet
        elif c.islower() and mod == 32:
            work_string = rus_lower_alphabet  
        # build new index = (old index + key) % mod
        new_index = (work_string.index(c) + key) % mod
        result_phrase += work_string[new_index]
    return result_phrase

# decode eng version
def decode(key, phrase):
    result_phrase = ''
    mod = 26
    for c in phrase:
        work_string = ''
        if c in symbols:
            result_phrase += c
            continue
        if c.isupper():
            work_string = eng_upper_alphabet
        elif c.islower():
            work_string = eng_lower_alphabet
      
        # build new index = (old index + key) % mod
        new_index = (work_string.index(c) + key) % mod
        result_phrase += work_string[new_index]
    return result_phrase

def main(decode_version, lang, key, txt):
    if decode_version == 'd':
        key = -key
    result = decode(key, txt, lang)
    print(result)

def list_to_key(lst):
    key_list = list()
    for str in lst:
        count = 0
        for c in str:
            if c.isalpha():
                count += 1
        key_list.append(count)
    return key_list

# run code
# main(decode_version, lang, key, txt)


# exe for caeser
text = 'Day, mice. "Year" is a mistake!'
text_list = text.split()
key_list = list_to_key(text_list)
print(text_list)
print(key_list)

dec_list = list()
for i in range(len(text_list)):
    dec_list.append(decode(key_list[i], text_list[i]))

print(dec_list)
print(' '.join(dec_list))


# for i in range(26):
#     main('d', 'en', i, text)


