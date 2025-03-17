line_one = input()

n = int(line_one.split()[0])
max = int(line_one.split()[1])

weights = list(map(int, input().split()))
weights.sort()

count = 0
l = 0
h = n - 1

while h >= l:
    if weights[l] + weights[h] <= max:
        l += 1
        h -= 1
        count += 1
    else:
        h -= 1
        count += 1

print(count)
    

