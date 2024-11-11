N = int(input())
A = list(map(int, input().split()))

# レートの区切りを定義
color = [399, 799, 1199, 1599, 1999, 2399, 2799, 3199, 4800]
# 対象のレートに何人いるかカウントするリスト
color_counts = [0] * 9

# レートに何人いるかカウント
for a in A:
    # どのレートに入るかを決める
    for i, rate in enumerate(color):
        if a <= rate:
            color_counts[i] += 1
            break

# レート3199までの色の数
normal_color = sum(1 for i in range(8) if color_counts[i] > 0)
# レート3200以上の数
free_color = color_counts[8]

# 色の種類数の最小値を求める
# レート3200以上の人だけいる場合
if normal_color == 0 and free_color >= 1:
    # 色の種類の最小値は 1 になる（何色にでもなれるため一つに限定）
    min_ans = 1
# レート3199までの人がいる場合、それらの数になる
else:
    min_ans = normal_color
    
# 色の種類数の最大値を求める
max_ans = normal_color + free_color

print(min_ans, max_ans)


# 計算量 O(N)


'''
# ---別解---
for a in A:
    if a >= 3200:
        color_counts[8] += 1
    else:
        # 400区切りでリストに格納
        rate = a // 400
        color_counts[rate] += 1
'''