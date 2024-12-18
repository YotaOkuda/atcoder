DIVISOR = 10 ** 9 + 7

N, M = map(int, input().split())
# A = [int(input()) for _ in range(M)]

dp = [0] * (N + 1)

for _ in range(M):
    n = int(input())
    dp[n] = -1

count = 0
for i in range(1, N + 1):
    if dp[i] == -1:
        continue    
    
    if i - 1 >= 0 and dp[i - 1] != -1:
        dp[i] += 1
    
    if i - 2 >= 0 and dp[i - 2] != -1:
        dp[i] += 1
    
    if dp[i] >= 2:
        count += dp[i]
    #count *= dp[i]
    count %= DIVISOR
        
print(count)