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
cnt = 0
a,b = 0,0
D = []

for i,j in Counter(A).most_common():
    if j >= 4:
        D.append(i)
        D.append(i)
    elif j >= 2:
        D.append(i)
        
D.sort()

if len(D) >= 2:
    print(D[-1]*D[-2])
else:
    print(0)