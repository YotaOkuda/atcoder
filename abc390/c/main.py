'''
<方針>
- 黒マスが存在する「上、下、左、右」の端の位置を求める（= 黒マスを全て使った長方形を求めるのと同義）
- 求めた範囲内に白マスがあれば不可となる
'''

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 端の値を初期化
left, top = 10000, 10000
right, under = -1, -1

# 端の位置を求める
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            left = min(left, w)
            right = max(right, w)
            top = min(top, h)
            under = max(under, h)

# 範囲内が黒マス、まだ塗られていないマスだけか判定するフラグ
flag = True
# 範囲内に黒マス、まだ塗られていないマスだけか探索する
for h in range(top, under + 1):
    for w in range(left, right + 1):
        # 白マスなら不可
        if S[h][w] == '.':
            flag = False
            break

print('Yes' if flag else 'No')

# 計算量 O(H * W)