import copy

H, W, K = map(int, input().split())
C = []
for _ in range(H):
    C.append(list(input()))

ans = 0

# 行と列の組み合わせをビット全探索
for num_H in range(1 << H):
    for num_W in range(1 << W):
        
        # Cを書き換えるためにコピー
        tmp_C = copy.deepcopy(C) 
        
        # 行を選択するかどうか判断
        for shift_H in range(H):
            # 行を選択するなら
            if 1 & (num_H >> shift_H) == 1:
                # 行を赤に塗り替える
                for w in range(W):
                    tmp_C[shift_H][w] = "x"
                
        # 列を選択するか判断
        for shift_W in range(W):
            # 列を選択するなら
            if 1 & (num_W >> shift_W) == 1:
                # 列を赤に塗り替える
                for h in range(H):
                    tmp_C[h][shift_W] = "x"
        
        # 黒の数をカウント
        count = sum([row.count('#') for row in tmp_C])                    
        
        # 黒の数が K と一致するなら、その行と列の選び方をカウント
        if count == K:
            ans += 1

print(ans)


# 計算量 O(2^(H + W) * H * W) < 147,456 < 10^8