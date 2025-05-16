'''
<方針>
- A, B はそれぞれ'#' が出現するSi の最小値i と最大値i
- C, D はそれぞれSi[j] の'#' が出現する最小値j と最大値j
'''
min_i, max_i = 11, 0
min_j, max_j = 11, 0

for i in range(10):
    S = str(input())
    for j in range(10):
        if S[j] == '#':
            min_i = min(min_i, i)
            max_i = max(max_i, i)
            min_j = min(min_j, j)
            max_j = max(max_j, j)

print(min_i + 1, max_i + 1)
print(min_j + 1, max_j + 1)

# 計算量 O(1)
