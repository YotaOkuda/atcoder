'''
<方針>
- DP で解く
- dp[i] は i 段目への移動方法を表す
- dp[i] に行く方法は dp[i - 1] + dp[i - 2] 通りになる
'''

# 割る数
DIVISOR = 10 ** 9 + 7

N, M = map(int, input().split())

# DP 用の配列
dp = [0] * (N + 1)

# 壊れている階段は -1 にしておく
for _ in range(M):
    n = int(input())
    dp[n] = -1

# 0 段目を初期化
dp[0] = 1

# dp[1], dp[2], ..., dp[N] を求める
for i in range(N + 1):
    # 壊れている足場はスキップ
    if dp[i] == -1:
        continue
    
    # 1 つ前の足場から移動する場合
    if i - 1 >= 0 and dp[i - 1] != -1:
        dp[i] += dp[i - 1]
    
    # 2 つ前の足場から移動する場合
    if i - 2 >= 0 and dp[i - 2] != -1:
        dp[i] += dp[i - 2]
    
    dp[i] %= DIVISOR
        
print(dp[N])

# 計算量 O(N)