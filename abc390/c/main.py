H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

left, top = 10000, 10000
right, under = -1, -1

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            left = min(left, w)
            right = max(right, w)
            top = min(top, h)
            under = max(under, h)
            
# print(f'top:{top}, under:{under}, left:{left}, right:{right}')

ans = True
for h in range(top, under + 1):
    for w in range(left, right + 1):
        if S[h][w] == '.':
            ans = False
            break

print('Yes' if ans else 'No')        