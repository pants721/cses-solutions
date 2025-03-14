def number_spiral(y: int, x: int) -> int:
    outer = max(y, x)
    inner = min(y, x)

    ans = (outer - 1) * (outer - 1)

    if (outer == y and outer % 2 != 0) or (outer == x and outer % 2 == 0):
        add = inner
    else:
        add = 2 * outer - inner

    return ans + add

n = int(input())
pairs = list()

for _ in range(n):
    l = input()    
    nums = list(map(int, l.split()))
    pairs.append(nums)

for pair in pairs:
    print(number_spiral(pair[0], pair[1]))
