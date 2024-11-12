N = int(input())
A = [int(input()) for _ in range(N)]

flag = False
i = 0
ans = 0

while flag == False:
    i = A[i] - 1  # 次のボタンの位置を記憶
    ans += 1
    if i == 1:  # ボタン2が光っていたら
       flag = True 
    if ans > N:  # N回探索しても、ボタン2が光らなかった場合
        ans = -1
        break

print(ans)