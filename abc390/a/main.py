'''
<方針>
- 隣り合う 2 つの項を入れ替える組み合わせは、合計で 4 回
- A を都度コピーして、1 回の入れ替えを行い昇順になっているか判定する
'''

A = list(map(int, input().split()))

# 判定用の答え
ans = [1, 2, 3, 4, 5]

# 昇順になっているかを判定するフラグ
flag = False

# 入れ替えを 4 回行う
for i in range(4):
    copied_A = A[:]
    copied_A[i], copied_A[i + 1] = copied_A[i + 1], copied_A[i]
    if copied_A == ans:
        flag = True

print('Yes' if flag else 'No')

# 計算量 O(1)