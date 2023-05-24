import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(i+1,N):
        s = 0
        for k in range(D):
            s += (X[i][k]-X[j][k])**2
        s = sqrt(s)
        if s%floor(s) == 0:
            cnt += 1

print(cnt)