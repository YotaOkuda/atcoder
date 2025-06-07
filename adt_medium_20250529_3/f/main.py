'''
<方針>
- 外積を求めて、負の符号ならば凸ではない
'''

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

points = [A, B, C, D]
flag = True

def is_convex(prev_pt, curr_pt, next_pt):
    v1 = (next_pt[0] - curr_pt[0], next_pt[1] - curr_pt[1])
    v2 = (prev_pt[0] - curr_pt[0], prev_pt[1] - curr_pt[1])
    cross = v1[0]*v2[1] - v1[1]*v2[0]
    return cross > 0

n = len(points)
for i in range(n):
    prev_pt = points[(i-1) % n]
    curr_pt = points[i]
    next_pt = points[(i+1) % n]
    if not is_convex(prev_pt, curr_pt, next_pt):
        flag = False
        break

print('Yes' if flag else 'No')

# 計算量 O(N)
