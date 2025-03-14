def tower(n: int, source: int, dest: int, aux: int):
    if n == 0:
        return
    tower(n - 1, source, aux, dest)
    print(f"{source} {dest}")
    tower(n - 1, aux, dest, source)

n = int(input())
print(pow(2, n) - 1)
tower(n, 1, 3, 2)
