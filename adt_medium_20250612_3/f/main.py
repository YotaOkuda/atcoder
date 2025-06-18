'''
<方針>
- M 以下の N 個の数字を使用して、合計が K 以下になるような数列を考える 
'''

N, M, K = map(int, input().split())

dp = [[0] * K for _ in range(N)]

dp[0][0] = 1
for i in range(N):
    for j in range(1, K):
        # M 以下の制限を考える
        dp[i][j] = dp[i][j] + i

