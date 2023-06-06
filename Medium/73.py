import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

a,b,c = map(int, input().split())

if c-a-b < 0:
    print("No")
else:
    if 4*a*b < (c-a-b)**2:
        print("Yes")
    else:
        print("No")

# from decimal import *
# a,b,c=map(int,input().split())
# a,b,c=Decimal(a),Decimal(b),Decimal(c)
# if c**Decimal(0.5)>a**Decimal(0.5)+b**Decimal(0.5): #Decimalモジュールを用いることで十分な精度で平方根の不等式を判定できる
#  print('Yes')
# else:
#  print('No')
