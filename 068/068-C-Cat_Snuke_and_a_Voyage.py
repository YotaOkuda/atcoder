N, M = map(int, input().split())

G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    G[a].append(b)
    G[b].append(a)

for i in G[0]:
    ans = (N - 1) in G[i]
    if ans:
        break

if ans:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')