n = int(input())

times = []

for _ in range(n):
    times.append(tuple(map(int, input().split())))

times.sort(key=lambda x: x[1])

watched = 0
time_elapsed = 0

for time in times:
    start, end = time 
    if start >= time_elapsed:
        watched += 1
        time_elapsed = end

print(watched)
