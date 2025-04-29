'''
<方針>
- dp[i][j](j=0, 1, 2, ... , W)
'''
N, W = map(int, input().split())

w = []
v = []
for i in range(N):
    goods = list(map(int, input().split()))
    w.append(goods[0])
    v.append(goods[1])

dp = [[-1] * (W + 1) for _ in range(N + 1)]

dp[0] = [0] * (W + 1)

ans = 0
for i in range(N):
    for j in range(W + 1):
        if j - w[i] >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w[i]] + v[i])

        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])


print(dp[N][W])
