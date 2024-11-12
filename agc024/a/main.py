A, B, C, K = map(int, input().split())

if K%2 == 0:
    ans = A - B
else:
    ans = B - A
    
if abs(ans) > 10**18:
    print('Unfair')
else:
    print(ans)
    
# 周期性
# Kが偶数の時は答えはA-B
# Kが奇数の時は答えはB-A

# 計算量 O(1)