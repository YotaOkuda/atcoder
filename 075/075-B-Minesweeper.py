H, W = map(int, input().split())
S = [input() for i in range(H)]

DI = [-1, -1, 0, 1, 1, 1, 0, -1]
DJ = [0, -1, -1, -1, 0, 1, 1, 1]

def mineCount(i, j):
    count = 0
    for di, dj in zip(DI, DJ):
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= H or nj >= W:
            continue
        if S[ni][nj] == '#':
            count += 1
    return count

results = []
for i in range(H):
    result = ''
    for j in range(W):
        if S[i][j] == '.':
            result = result + (str(mineCount(i, j)))
        else:
            result = result + '#'
    results.append(result)

for answer in results:
    print(answer)

