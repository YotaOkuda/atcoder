'''
<方針>
- 毎回 K <= i のときの Ai の値を計算していると、TLE になってしまう
- Ak の値をあらかじめ求めておく
- Ak+1, Ak+2 と見ていくと、A0, A1 は計算から外れていく
- Ak を total_valueとして、 Ak+1 のときに範囲外となる値 left_value を引いていく
- total_value は Ai * 2 となる
'''

import sys

N, K = map(int, input().split())

mod = 10 ** 9

# N <= K の場合
if N < K:
    print(1)
    sys.exit()
elif N == K:
    print(K)
    sys.exit()

# リスト A を用意
A = [1] * (N + 1)
# Ak の値を求めておく
A[K] = K
total_value = K * 2

# Ak+1 からAn まで求めていく
for i in range(K + 1, N + 1):
    left_value = A[i - K - 1]
    A[i] = total_value - left_value

    A[i] = A[i] % mod

    total_value = A[i] * 2


print(A[N])

# 計算量 O(N)