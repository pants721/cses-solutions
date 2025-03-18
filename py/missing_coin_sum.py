n = int(input())
arr = list(map(int, input().split()))

arr.sort()

val = 1

for i in range(n):
    if arr[i] > val:
        print(val)
        exit()
    elif arr[i] <= val:
        val += arr[i]

print(val)


