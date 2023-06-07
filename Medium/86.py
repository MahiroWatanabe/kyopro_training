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
D = Counter(A)
k = list(D.keys())
v = list(D.values())

if len(D) == 1 and 0 in k:
    print("Yes")
elif len(D) == 2 and 0 in k and (v[0] == v[1]*2 or v[1] == v[0]*2):
    print("Yes")
elif len(D) == 3 and k[0]^k[1]^k[2] == 0 and v[0] == v[1] == v[2]:
    print("Yes")
else:
    print("No")