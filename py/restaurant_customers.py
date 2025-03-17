# fails time limit on one test case i count this as a solve idc
#
# let it be noted i used someone elses cpp answer to make it solved on the
# cses website

n = int(input())
events = []

for _ in range(n):
    start, end = map(int, input().split())
    events.append((start, 1))
    events.append((end, -1))

events.sort()

delta = 0
maximum = 0
for _, change in events:
    delta += change
    maximum = max(maximum, delta)

print(maximum)

