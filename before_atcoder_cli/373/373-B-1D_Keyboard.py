S = list(input())

# キーボードの入力順は固定
list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ans = 0
pre = S.index('A')  # スタート位置

# 入力順に位置を見つけていく
for s in list:
    cur = S.index(s)
    ans += abs(pre - cur)  # 指の移動距離を計算
    pre = cur
    
print(ans)


# 計算量 O(1)