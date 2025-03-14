n = int(input())
s = f'{n} '

while n != 1:
    if n % 2 == 0:
        n /= 2
        n = int(n)
    else:
        n *= 3
        n += 1
    s += f'{n} '

print(s)


