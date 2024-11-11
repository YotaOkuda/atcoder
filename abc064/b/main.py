N = int(input())
A = list(map(int, input().split()))

# 最大座標から最小座標を引く = 最小の移動距離
print(max(A) - min(A))


# 計算量 O(1)