N = int(input())

INF = 110000
dp = [INF] * (N + 1)
dp[0] = 0

pow6, pow9 = [], []
base6, base9 = 1, 1
while base6 <= N:
    pow6.append(base6)
    base6 *= 6
while base9 <= N:
    pow9.append(base9)
    base9 *= 9

for i in range(1, N + 1):
    for x in pow6:
        if i - x >= 0:
            dp[i] = min(dp[i], dp[i - x] + 1)
    for y in pow9:
        if i - y >= 0:
            dp[i] = min(dp[i], dp[i - y] + 1)
        
print(dp[N])