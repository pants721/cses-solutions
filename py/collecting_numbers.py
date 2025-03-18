n = int(input())
arr = list(map(int, input().split()))

indices = {num: idx for num, idx in zip(arr, range(n))}

rounds = 1

for i in range(1, n):
    if indices[i + 1] < indices[i]:
        rounds += 1

print(rounds)
