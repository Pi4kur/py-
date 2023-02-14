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