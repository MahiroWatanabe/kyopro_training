import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N = int(input())
D = defaultdict(int)
ans = []

for _ in range(N):
    S = input()
    D[S] += 1

current_value = 0

for key,value in D.items():
    current_value = max(current_value,value)

for key,value in D.items():
    if value == current_value:
        ans.append(key)

ans.sort()
print(*ans)