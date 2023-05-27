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
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for order in permutations(XY,N):
    num = 0
    for i in range(N-1):
        num += sqrt((order[i][0]-order[i+1][0])**2+(order[i][1]-order[i+1][1])**2)
    ans += num        

print(ans/factorial(N))