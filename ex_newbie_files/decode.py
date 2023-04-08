# xxxxx2[xxx3[xx4[abcd]xx]xxx]xxxxx
# to
# y1 = 4[abcd] -> abcdabcdabcd
# y2 = 3[xxy1xx] -> xxy1xxxxy1xxxxy1xx -> xxabcdabcdabcdxxxxabcdabcdabcdxxxxabcdabcdabcdxx
# y3 = 2[xxxy2xxx] -> xxxxxabcdabcdabcdxxxxabcdabcdabcdxxxxabcdabcdabcdxxxxxxxxxxabcdabcdabcdxxxxabcdabcdabcdxxxxabcdabcdabcdxxxxx
# xxxxx-xxx xxxxx

text1 = 'ab2[b2[cd]3[e]]'
text_sam_1 = 'x2[yy3[ff4[a]dd]kkk]zzz'
# abbcdcdeeebcdcdeee
text2 = '[[[][[][]]][]]'

def brackets_index(text):
    count = 0
    index_dict = {}
    temp_list = []

    for i in range(len(text)):
        if text[i] == '[':
            count += 1
            temp_list.append(i)
        elif text[i] == ']':
            count -= 1
            index_dict[temp_list.pop()] = i

    if count == 0:
        print('valid')
    else:
        print('not valid')
    return index_dict


def decode(text):
    print('Deconde from:', text)
    print('Creat dictionary with indexes of bracket')
    my_dict = brackets_index(text)
    print(my_dict)
    answer = ''
    k = 0
    i = 0
    while i < len(text):
        if text[i].isalpha():
            answer += text[i]
            i += 1
        elif text[i].isdigit():
            k = k * 10 + int(text[i])
            i += 1
        elif text[i] == '[':
            end_index = my_dict.get(i)
            answer += decode(text[i+1 : end_index]) * k
            i = end_index + 1
            k = 0

        print(answer, 'from i:', i, k)
        # elif text[i] == ']':
        #     ignore_writing_flag = False
        
    return answer
string = decode(text1)
print(string)
if string == 'abbcdcdeeebcdcdeee':
    print('yes')
else:
    print('no')
# my_dict = brackets_index(text2)
# print(my_dict)