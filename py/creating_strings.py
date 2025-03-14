from itertools import permutations

s = input()

perms = set([''.join(p) for p in permutations(s)])
print(len(perms))
for perm in sorted(perms):
    print(perm)
