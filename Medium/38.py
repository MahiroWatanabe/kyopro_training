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
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

D_N = defaultdict(int)
for i in D:
    D_N[i] += 1

for i in T:
    if D_N[i] >= 1:
        D_N[i] -= 1
    else:
        print("NO")
        exit()

print("YES")