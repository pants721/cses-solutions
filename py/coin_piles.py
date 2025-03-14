def can_empty(a: int, b: int) -> bool:
    if (2 * a - b) % 3 != 0 or (2 * a - b) < 0 or (2 * b - a) % 3 != 0 \
        or (2 * b - a) < 0:
        return False
    return True

t = int(input())
pairs = list()

for _ in range(t):
    pair = list(map(int, input().split()))
    pairs.append(pair)

for pair in pairs:
    if can_empty(pair[0], pair[1]):
        print("YES")
    else:
        print("NO")
