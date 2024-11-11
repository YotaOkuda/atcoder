a, b, c = map(int, input().split())

# 3 つのうち 2 個選んだ時の値段を計算
ab = a + b
bc = b + c
ac = a + c

# 最小値を出力
print(min(ab, bc, ac))


# 計算量 O(1)