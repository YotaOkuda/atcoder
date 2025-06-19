'''
<方針>
- M 以下の N 個の数字を使用して、合計が K 以下になるような数列を考える 
- dp[i][j] は i 項目まで決めた時に、値が丁度 j になる総数
- dp[i] から dp[i + 1] へ項を増やした時の遷移を考える
- j + k(1 から M + 1) <= K ならば dp[i + 1][j + k] に dp[i][j] を加算する
- dp[N][j] の総和が K 以下の総数
'''

N, M, K = map(int, input().split())

mod = 998244353

dp = [[0] * (K + 1) for _ in range(N + 1)]

dp[0][0] = 1
for i in range(N):
    for j in range(K + 1):
        if dp[i][j] == 0:
            continue
        for k in range(1, M + 1):
            if j + k <= K:
                dp[i + 1][j + k] += dp[i][j]
                dp[i + 1][j + k] %= mod

ans = 0
for j in range(K + 1):
    ans += dp[N][j]

print(ans % mod)

# 計算量 O(NMK)
