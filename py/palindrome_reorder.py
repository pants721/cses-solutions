from collections import Counter
import math

counts = Counter(sorted(list(input())))

res = ''
middle = ''

for c, count in counts.items():
    sub_s = [c for _ in range(math.floor(count / 2))]
    res += ''.join(sub_s)
    if count % 2 != 0:
        if middle == '':
            middle = c
        else:
            print("NO SOLUTION")
            exit()

print(res + middle + res[::-1])
