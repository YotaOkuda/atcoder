C = [list(map(int, input().split())) for i in range(3)]

found = False

for a1 in range(101):   
    b1_a1 = C[0][0] - a1    # a1を固定したときのb1,b2,b3の取りうる値を決める
    b2_a1 = C[0][1] - a1
    b3_a1 = C[0][2] - a1
    for a2 in range(101):
        b1_a2 = C[1][0] - a2    # a2を固定したときのb1,b2,b3の取りうる値を決める
        b2_a2 = C[1][1] - a2
        b3_a2 = C[1][2] - a2
        for a3 in range(101):
            b1_a3 = C[2][0] - a3    # a3を固定したときのb1,b2,b3の取りうる値を決める
            b2_a3 = C[2][1] - a3
            b3_a3 = C[2][2] - a3

            # 各a1~3の時に決定したb1~3の値が一致しているか、負の値は除外
            if (b1_a1 == b1_a2 == b1_a3 and
                b2_a1 == b2_a2 == b2_a3 and
                b3_a1 == b3_a2 == b3_a3 and
                min(b1_a1, b1_a2, b1_a3, b2_a1, b2_a2, b2_a3, b3_a1, b3_a2, b3_a3) >= 0):
                found = True
                break
        if found:
            break
    if found:
        break

if found:
    print('Yes')
else:
    print('No')

# 計算量O(N^3) = 100^3 < 10^8



# 公式解答
C = [list(map(int, input().split())) for i in range(3)]

# x[0]は0でも問題ないので最初から決めておく
x = [0, 0, 0]
y = [0, 0, 0]

# xを決めたことによるy,yを決めたことによるxを計算
for i in range(3):
    y[i] = C[0][i] - x[0]
for i in range(3):
    x[i] = C[i][0] - y[0]

flag = True

# x[i] + y[j]がC[i][j]と一致するかどうか
for i in range(3):
    for j in range(3):
        if x[i] + y[j] != C[i][j]:
            flag = False

if flag:
    print('Yes')
else:
    print('No')