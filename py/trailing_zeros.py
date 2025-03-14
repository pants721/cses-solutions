import math
n = int(input())

k = 1
sum = 0

while pow(5, k) <= n:
    sum += math.floor(n / pow(5, k))
    k += 1

print(sum)
