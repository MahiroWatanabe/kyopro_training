import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext


def calc_divisors(N):
    D = defaultdict(int)

    for i in range(1, N + 1):
        if i * i > N:
            break
        
        if N % i != 0:
            continue

        D[i] = N //i
    return D

N = int(input())
ans = 10**18
res = calc_divisors(N)

for key, value in res.items():
    ans = min(ans,key-1+value-1)
    
print(ans)