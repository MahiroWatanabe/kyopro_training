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
D = defaultdict(bool)
cnt = 0

for _ in range(N):
    A = int(input())
    D[A] = not D[A]

for value in D.values():
    if value:
        cnt += 1

print(cnt)