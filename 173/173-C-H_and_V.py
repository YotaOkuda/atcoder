import copy

H, W, K = map(int, input().split())
C = []
for _ in range(H):
    C.append(list(input()))

ans = 0

for num_H in range(1 << H):
    for num_W in range(1 << W):
        # Cを書き換えるためにコピー
        tmp_C = copy.deepcopy(C) 
        
        # 行を選択するかどうか
        for shift_H in range(H):
            if 1 & (num_H >> shift_H) == 1:
                # print(f'shift_H:{shift_H}')
                for w in range(W):
                    tmp_C[shift_H][w] = "x"  # 行を黒に塗り替える
                
        # 列を選択するかどうか
        for shift_W in range(W):
            if 1 & (num_W >> shift_W) == 1:
                # print(f'shift_W:{shift_W}')
                for h in range(H):
                    tmp_C[h][shift_W] = "x"
        
        count = sum([row.count('#') for row in tmp_C])                    
        if count == K:
            ans += 1

print(ans)