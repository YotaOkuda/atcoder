H, W = map(int, input().split())
A = [input() for i in range(H)]

result_h = []
new_H = 0
for h in range(H):
    if A[h] != '.'*W:
        result_h.append(A[h])
        new_H += 1

result_w =['' for n in range(new_H)]
for w in range(W):
    count = 0
    for h in range(new_H):
        if result_h[h][w] == '.':
            count += 1
    if count != new_H:
        for n in range(new_H):
            result_w[n] = result_w[n] + result_h[n][w]

for answer in result_w:
    print(answer)