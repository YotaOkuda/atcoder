import sys

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))


if 1 not in X or sum(A) != N or N - X[-1] + 1 < A[-1]:
    print(-1)
    sys.exit()


# 操作回数
count = 0
# X[i + 1] の場所に持ち越しのコマ
next_koma = 0
flag = True

i = 0
while i < M:
    if i == M - 1:
        count += sum(range(1, N - X[i] + 1))
        break
    
    # 空きマス
    distance = X[i + 1] - X[i] - 1
    # A[i - 1] から持ち越されたコマを加算
    A[i] += next_koma
    # 手持ちのコマで、空きマスを埋められるか
    if A[i] <= distance:
        flag = False
        break
    
    # 空きマスを埋めるのに必要な操作回数を加算
    count += sum(range(1, distance + 1))
    
    # 余ったコマは、X[i + 1] マスに持ち越し
    next_koma = X[i] - distance - 1
    # 余ったコマをがあれば
    if next_koma > 0:
        # X[i + 1] まで移動させるのに必要な操作回数を加算
        count += (distance + 1) * next_koma
        
    # i を更新
    i += 1
    
# 答えを出力
if flag:
    print(count)
else:
    print(-1)