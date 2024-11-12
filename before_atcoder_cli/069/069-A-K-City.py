n, m = map(int, input().split())

# 街区の数は各線 - 1 を掛けた値になる
print((n - 1) * (m - 1))

# 計算量 O(1)