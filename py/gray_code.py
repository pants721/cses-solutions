n = int(input())
res = [0]
for i in range(1, 2**n):
    res.append(res[-1] ^ (i & -i))
for c in res:
    ans = bin(c).lstrip('0b')
    ans = '0' * (n - len(ans)) + ans
    print(ans)
