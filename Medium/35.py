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

def f(x,c,d):
    result = x
    result -= x//c
    result -= x//d
    result += x//lcm(c,d)
    
    return result

A,B,C,D = map(int, input().split())

print(f(B,C,D)-f(A-1,C,D))