'''
<方針>
- 前回との差分が S + 0.5 を超えないかチェックする
'''
N, S = map(int, input().split())
T = list(map(int, input().split()))

flag = True
start = 0
for i in range(N):
    progress = T[i] - start
    if progress >= S + 0.5:
        flag = False
    start = T[i]

print('Yes' if flag else 'No')

# 計算量 O(N)
