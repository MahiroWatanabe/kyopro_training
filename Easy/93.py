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
A = list(map(int,input().split()))
D = list(accumulate(A))
S = sum(A)
ans = 10**18

for i in range(N-1):
    diff = S-D[i]
    if diff == S//2:
        print(0)
        exit()
    else:
        ans = min(ans,abs(D[i]-diff))

print(ans)