N = int(input())

dp = [N + 1] * (N + 1)
dp[0] = 1
dp[1] = 1

def generate_powers(limit):
    powers = set()
    value1, value2 = 6, 9
    while value1 <= limit:
        powers.add(value1)
        value1 *= value1
        
    while value2 <= limit:
        powers.add(value2)
        value2 *= value2
    
    return powers

powers = generate_powers(N)

for i in range(1, N + 1):
    if i in powers:
        dp[i] = 1
    else:
        for j in range(1, i // 2 + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])
        
print(dp[N])
# print(dp)