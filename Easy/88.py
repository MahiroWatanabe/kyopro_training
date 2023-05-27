import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

D = defaultdict(int)
ans = 0

N = int(input())
for _ in range(N):
    s = input()
    D[s] += 1

M = int(input())
for _ in range(M):
    t = input()
    D[t] -= 1

for value in D.values():
    ans = max(ans,value)

print(ans)