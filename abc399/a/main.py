'''
<方針>
- 先頭から順に比べていく
'''

N = int(input())
S = str(input())
T = str(input())

ans = 0
for i in range(N):
    if S[i] != T[i]:
        ans += 1

print(ans)

# 計算量 O(N)