'''
<方針>
- "2"を見つけたら ans に追加していく
'''

S = str(input())

ans = ""
for i in range(len(S)):
    if S[i] == "2":
        ans += "2"

print(ans)

# 計算量 O(len(S))