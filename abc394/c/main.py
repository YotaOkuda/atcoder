'''
<方針>
- 先頭から操作を行うと戻りが発生するので、末尾から操作を行う
'''

S = list(str(input()))

# 末尾から操作を行う
for i in range(len(S) - 1, 0, -1):
    # 'WA' を見つけたら 'AC' に変える
    if S[i - 1] == 'W' and S[i] == 'A':
        S[i - 1] = 'A'
        S[i] = 'C'

print(*S, sep='')

# 計算量 O(len(S))