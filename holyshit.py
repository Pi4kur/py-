new_dict = dict()
new_dict.update({1 : 2})
new_dict.update({3 : 5})
new_dict.update({4 : 7})
print(new_dict)
new_dict.update({2: None})
print(new_dict)
new_dict.update({2: 9})
print(new_dict)
x = new_dict.popitem()
print(new_dict)
print(x)


