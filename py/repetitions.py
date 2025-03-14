import itertools

s = input()
print(max(map(len, ["".join(grp) for _, grp in itertools.groupby(s)])))
