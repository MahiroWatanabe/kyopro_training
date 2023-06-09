import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def prime_factorize(N):
    D = defaultdict(int)
    if N == 1:
        D[1] += 1
        return D
    i = 2
    while i*i <= N:
        if N%i == 0:
            D[i] += 1
            N //= i
        else:
            i += 1
    if N != 1:
        D[N] += 1
    
    return D

N,P = map(int, input().split())
D = prime_factorize(P)
ans = 1

for i,j in D.items():
    ans *= i**(j//N)

print(ans)