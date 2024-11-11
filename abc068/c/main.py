N, M = map(int, input().split())

G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    G[a].append(b)
    G[b].append(a)

# 島１を探索
for i in G[0]:
    ans = (N - 1) in G[i]   # 島１に隣接する島から島Nに行けるか（２つの便でゴールできるか）
    if ans:
        break

if ans:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')