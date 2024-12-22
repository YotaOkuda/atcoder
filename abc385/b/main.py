'''
<方針>
- 愚直にシミュレーションする
- すでに通った家は位置をリストに記録しておく
'''

H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = list(str(input()))

# 通った家の位置を記録するセット（リストより計算量が少ない）
is_passing = set()
# 通った家の数をカウント
count = 0

# 位置を 0 ベースに合わせる
H, W, X, Y = H - 1, W - 1, X - 1, Y - 1

# 文字を一つづつ処理していく
for t in T:
    # 文字が U のとき
    if t == 'U' and X - 1 >= 0:
        # 通行可能かチェック
        if S[X - 1][Y] != '#':
            # 現在位置を更新
            X -= 1
            # 未通過の家の場合
            if S[X][Y] == '@' and (X, Y) not in is_passing:
                is_passing.add((X, Y))
                count += 1
                
    if t == 'D' and  X + 1 <= H:
        if S[X + 1][Y] != '#':
            X += 1
            if S[X][Y] == '@' and (X, Y) not in is_passing:
                is_passing.add((X, Y))
                count += 1
            
    if t == 'L' and Y - 1 >= 0:
        if S[X][Y - 1] != '#':
            Y -= 1
            if S[X][Y] == '@' and (X, Y) not in is_passing:
                is_passing.add((X, Y))
                count += 1
        
    if t == 'R' and Y + 1 <= W:
        if S[X][Y + 1] != '#':
            Y += 1
            if S[X][Y] == '@' and (X, Y) not in is_passing:
                is_passing.add((X, Y))
                count += 1

print(X + 1, Y + 1, count)

# 計算量 O(T)