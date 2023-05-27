import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def lcm(A,B):
    return (A*B)//gcd(A,B)

N = int(input())
a = list(map(int,input().split()))
L = a[0]
ans = 0

for i in range(1,N):
    L = lcm(L,a[i])

for i in a:
    ans += (L-1)%i

print(ans)