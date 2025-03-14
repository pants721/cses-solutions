def permutations(n: int) -> str:
    if n == 2 or n == 3:
        return "NO SOLUTION"
    odd = [x for x in range(1, n + 1, 2)]
    even = [x for x in range(2, n + 1, 2)]
    if n == 4:
        odd = odd[::-1]
        even = even[::-1]
    return " ".join(map(str, (odd + even)))
 
print(permutations(int(input())))
