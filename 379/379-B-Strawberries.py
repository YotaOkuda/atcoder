'''
<方針>
notion 追加
'''

N, K = map(int, input().split())
S = input()

i, count = 0, 0
ans = 0

while i < len(S):
    if S[i] == 'O':
        count += 1
    else:
        count = 0
    
    if count >= K:
        ans += 1
        count -= K
    
    i += 1
    
print(ans)