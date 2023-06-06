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
S = sum(A)
ans = 10**18
D = list(accumulate(A))

for i in range(N-1):
    ans = min(ans,abs(D[i]-(S-D[i])))

print(ans)

# N = int(input())
# A = list(map(int,input().split()))
# x,y = 0,sum(A)
# ans = 10**18

# for i in range(N-1):
#     x += A[i]
#     y -= A[i]
#     ans = min(ans,abs(x-y))

# print(ans)