'''
<方針>
- 出現した行と、列を重複がないように記録する
- 行、列ごとに盤面を塗り替える
- 最後に '.' の個数をカウントする
'''

S = []
for i in range(8):
    S.append(list(input()))

# 出現した行を保持
w_set = set()
# 出現した列を保持
h_set = set()

# 出現した位置をカウント
for i in range(8):
    for j in range(8):
        if S[i][j] == '#':
            w_set.add(i)
            h_set.add(j)

# 行を '#' に塗り替える
for w in w_set:
    for h in range(8):
        S[w][h] = '#'
        
# 列を '#' に塗り替える
for h in h_set:
    for w in range(8):
        S[w][h] = '#'

ans = 0
# '.' の数を数える
for i in range(8):
    for j in range(8):
        if S[i][j] == '.':
            ans += 1
            
print(ans)

# 計算量 O(1)