ans = 0

for i in range(1, 13):
    S = input()
    if i == len(S):
        ans += 1
        
print(ans)

# 計算量 O(1)