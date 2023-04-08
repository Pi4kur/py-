# num = 67
# num_2 = bin(num)
# print(num_2)
# strip_str = num_2[2:]
# winning = strip_str[1:] + strip_str[0]
# winning = winning.lstrip('0')
# winning = (num_2[:2] + winning)
# print(winning)
# dec = int(winning, base=2)
# print(dec)

# n, k = int(input()), int(input())
n, k = 7, 5
list_with_n = list(range(1,n+1))
print(*list_with_n)

def numberphile(n, k):
    if n == 1:
        return 1
    else:
        return ((numberphile(n-1,k) + k - 1) % n)+1

print(numberphile(n, k))