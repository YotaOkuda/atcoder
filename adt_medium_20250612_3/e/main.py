'''
<方針>
- 通常の再帰で求めていくと、TLE となる
- メモ化再帰を用いる
- python では @cache でメモ化することができる
'''

from functools import cache
N = int(input())

@cache
def f(N):
    if N == 1:
        return 0
    return f(N // 2) + f((N + 1) // 2) + N

print(f(N))

# 計算量 O(logN)
