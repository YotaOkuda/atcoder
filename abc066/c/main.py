n = int(input())
A = list(map(int, input().split()))

B = []

# a の個数が奇数個の場合　
if len(A) % 2 != 0:
    for i, a in enumerate(A):
        # 偶数個目の a は先頭に追加
        if i % 2 == 0:
            B.insert(0, a)
        # 奇数個目の a は最後尾に追加
        else:
            B.append(a)
# a の個数が偶数個の場合（奇数個と逆の操作）
else:
    for i, a in enumerate(A):
        if i % 2 == 0:
            B.append(a)
        else:
            B.insert(0, a)
            
print(' '.join(str(b) for b in B))

# 計算量 O(n^2)  reverse と同じだが TLE にはならない



# 以下だと TLE になる
# reverse の計算量は O(n), よって i 回目では O(i) かかる
# 1 ～ n までの reverse を合計すると O(n^2) となる
'''
for a in A:
    B.append(a)
    B.reverse()

print(' '.join(str(b) for b in B))
'''


'''
# ---さらに高速に---
from collections import deque
n = int(input())
A = list(map(int, input().split()))

# リストの先頭への追加を O(1) で行うために deque を使用
B = deque()

if len(A) % 2 != 0:
    for i, a in enumerate(A):
        if i % 2 == 0:
            B.appendleft(a)
        else:
            B.append(a)
else:
    for i, a in enumerate(A):
        if i % 2 == 0:
            B.append(a)
        else:
            B.appendleft(a)

print(' '.join(str(b) for b in B))

# 計算量 O(n)
'''