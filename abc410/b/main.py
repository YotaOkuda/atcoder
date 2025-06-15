'''
<方針>
- x が 1 以上なら答えに追加して、中身を増やす
- x が 1 未満なら最小のインデックス（最小の中で一番小さいインデックス）を答えに追加して、中身を増やす
'''

N, Q = map(int, input().split())
X = list(map(int, input().split()))

box = [0] * N
ans = []
for x in X:
    if x >= 1:
        ans.append(x)
        box[x - 1] += 1
    else:
        min_index = box.index(min(box))
        ans.append(min_index + 1)
        box[min_index] += 1

print(*ans)

# 計算量 O(len(X) * N)
