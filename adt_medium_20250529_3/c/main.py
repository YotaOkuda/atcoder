'''
<方針>
- 爆弾を見つけたら、全てのマスを見て爆破距離以内であれば、'.' にする
- '#' 壁の時のみ爆破する
- 爆弾の場所も'.' にする
'''

R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

boms = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# 爆弾を見つける
for r in range(R):
    for c in range(C):
        # 爆弾を見つけたら
        if B[r][c] in boms:
            bom = int(B[r][c])
            # 爆破距離以内の壁を見つける
            for i in range(R):
                for j in range(C):
                    dis = abs(r - i) + abs(c - j)
                    if dis <= bom and B[i][j] == '#':
                        B[i][j] = '.'
            # 爆弾の場所も '.' にする
            B[r][c] = '.'

for r in range(R):
    print(''.join(map(str, B[r])))

# 計算量 O((R*C)^2)
