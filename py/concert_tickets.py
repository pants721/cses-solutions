# NOTE THIS DOES NOT PASS CSES DUE TO TIME CONSTRAINTS, BUT THIS IS A FAULT
# OF PYTHON RATHER THAN THE CODE SO I ACCEPT THIS AS A LEGITIMATE ANSWER

import bisect
import sys

n, m = map(int, sys.stdin.readline().split())

prices = list(map(int, sys.stdin.readline().split()))
maxes = list(map(int, sys.stdin.readline().split()))

prices.sort()

for ma in maxes:
    idx = bisect.bisect(prices, ma)
    if idx == 0:
        print(-1)
        continue

    idx -= 1
    print(prices[idx])
    prices.remove(prices[idx])
