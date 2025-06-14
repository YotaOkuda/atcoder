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
