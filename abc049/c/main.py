'''
<方針>
- 動的計画法で解く
- dp[i] は S[0:i] が、各文字列のどれかと一致している場合 True にする
- 探索文字列前の dp が True の場合のみ、確認していく
- dp[1], d][2], ..., dp[N] を求め、dp[N] が True なら 'YES'
'''

S = str(input())
N = len(S)

# 動的計画法用の配列
dp = [False] * (N + 1)

# 初期条件
dp[0] = True

# dp[1], dp[2], ..., dp[N] を順に求める
for i in range(N + 1):
    if i >= 5 and dp[i - 5] and S[i - 5:i] == 'erase':
        dp[i] = True
    
    if i >= 6 and dp[i - 6] and S[i - 6:i] == 'eraser':
        dp[i] = True
    
    if i >= 5 and dp[i - 5] and S[i - 5:i] == 'dream':
        dp[i] = True
    
    if i >= 7 and dp[i - 7] and S[i - 7:i] == 'dreamer':
        dp[i] = True

print('YES' if dp[N] else 'NO')

# 計算量 O(N)