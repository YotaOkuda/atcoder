N = int(input())

ans = 1
mod = 0
for i in range(1, N + 1):
    ans = ans * i % (10**9 + 7)
    
print(ans)


# 計算量 O(N)