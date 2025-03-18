n = int(input())
lengths = list(map(int, input().split()))

lengths.sort()
mid = lengths[n // 2]
diff = 0

for length in lengths:
    diff += abs(mid - length)

print(diff)
