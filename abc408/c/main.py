N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]

wall = [0] * N
for i in range(M):
    L, R = LR[i][0] - 1, LR[i][1] - 1
    wall[L] += 1
    if R + 1 < N:
        wall[R + 1] -= 1

start = 0
for i in range(N):
    wall[i] = start + wall[i]
    start = wall[i]

print(min(wall))
