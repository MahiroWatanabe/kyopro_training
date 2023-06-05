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
ans = 0
for _ in range(N):
    S = input()
    D[S[0]] += 1

for i,j,k in combinations([i for i in "MARCH"],3):
    ans += D[i]*D[j]*D[k]

print(ans)