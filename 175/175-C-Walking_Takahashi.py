X, K, D = map(int, input().split())

X = abs(X)
q = X // D
r = X % D  # 最小地点

if X >= K*D:  # 移動距離がXより小さいならば一方向に進むだけ
    ans = X - K*D
elif (K - q)%2 == 0:  # rについてから偶数回移動するならrに戻れる
    ans = r
elif (K - q)%2 != 0:  # rについてから奇数回移動するならrに戻れない
    ans = abs(r - D)

print(ans)


# 計算量 O(1)