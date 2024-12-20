# 十分大きい値
INF = 2 ** 60

# 入力
N = int(input())
h = list(map(int, input().split()))

# 動的計画法用の配列（最小化問題なので INF で初期化）
dp = [INF] * N

# 初期条件（スタート地点へ移動するコストは 0）
dp[0] = 0

# 足場 1, 2, ..., N - 1 への最小コストを順に求める
for i in range(N):
    if i - 1 >= 0:
        dp[i] = min(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    
    if i - 2 >= 0:
        dp[i] = min(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

# 出力
print(dp[N - 1])