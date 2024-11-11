N = int(input())

ans = 1
mod = 0
for i in range(1, N + 1):
    ans = ans * i % (10**9 + 7)
    
print(ans)

# 最後に (10**9 + 7) で割るとTLEになる
# x で割った答えを最終的に出力するには、オーバーフローを考慮して毎回割る


# 計算量 O(N)