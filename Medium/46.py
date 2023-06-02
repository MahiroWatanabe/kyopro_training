import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

S = input()
D = Counter(S)
print("YES" if not (abs(D['a']-D['b'])>=2 or abs(D['b']-D['c'])>=2 or abs(D['c']-D['a'])>=2)else "NO")